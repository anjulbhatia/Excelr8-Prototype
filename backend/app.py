import pandas as pd
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from models import UploadResponse, CleanOptions, ReportRequest, ReportResponse
from utils import save_file, clean_data, generate_report
from config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Allow frontend demo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

# in-memory dataframe
DB = {"df": None, "filename": None}

@app.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile):
    path = save_file(file)
    DB["df"] = pd.read_csv(path)
    DB["filename"] = file.filename
    return UploadResponse(filename=file.filename, size=len(DB["df"]), message="File uploaded successfully")

@app.post("/clean")
async def clean(options: CleanOptions):
    if DB["df"] is None:
        return JSONResponse(status_code=400, content={"error": "No data uploaded"})
    df = clean_data(DB["df"], options.impute_missing, options.detect_outliers, options.validate_rules)
    DB["df"] = df
    return {"message": "Data cleaned", "rows": len(df)}

@app.post("/report", response_model=ReportResponse)
async def report(fmt: str = Form("html")):
    if DB["df"] is None:
        return JSONResponse(status_code=400, content={"error": "No data to report"})
    path = generate_report(DB["df"], fmt)
    return ReportResponse(report_path=path, message="Report generated")

@app.get("/download/{fmt}")
async def download(fmt: str):
    path = f"./reports/report.{fmt}"
    return FileResponse(path, filename=f"report.{fmt}")
