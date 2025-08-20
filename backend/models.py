from pydantic import BaseModel
from typing import List, Optional

class UploadResponse(BaseModel):
    filename: str
    size: int
    message: str

class CleanOptions(BaseModel):
    impute_missing: bool = False
    detect_outliers: bool = False
    validate_rules: bool = False

class ReportRequest(BaseModel):
    format: str  # "pdf" or "html"

class ReportResponse(BaseModel):
    report_path: str
    message: str
