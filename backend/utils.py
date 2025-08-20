import os
import pandas as pd
import numpy as np
from config import settings

def save_file(file) -> str:
    """save uploaded file."""
    path = os.path.join(settings.UPLOAD_DIR, file.filename)
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    with open(path, "wb") as f:
        f.write(file.file.read())
    return path

def clean_data(df: pd.DataFrame, impute=False, outliers=False, validate=False) -> pd.DataFrame:
    """cleaning."""
    if impute:
        df = df.fillna(df.mean(numeric_only=True))  # quick fake imputation
    if outliers:
        # Just cap at 3 std dev (demo only)
        for col in df.select_dtypes(include=[np.number]):
            df[col] = np.where(df[col] > df[col].mean() + 3*df[col].std(),
                               df[col].mean(), df[col])
    # validate = stub
    return df

def generate_report(df: pd.DataFrame, fmt="html") -> str:
    """Report generation."""
    os.makedirs(settings.REPORT_DIR, exist_ok=True)
    path = os.path.join(settings.REPORT_DIR, f"report.{fmt}")
    if fmt == "html":
        df.head().to_html(path)
    else:
        df.head().to_csv(path)  # fake pdf with csv for now
    return path
