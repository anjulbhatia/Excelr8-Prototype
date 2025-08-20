import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Excelr8"
    VERSION: str = "0.1.0"
    DEBUG: bool = True

    # paths or storage
    UPLOAD_DIR: str = "./uploads"
    REPORT_DIR: str = "./reports"

settings = Settings()
