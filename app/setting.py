from pydantic import BaseModel


class Settings(BaseModel):
    APP_TITLE: str = "Student Data API"
    APP_VERSION: str = "1.0.0"
    DOC_URL: str = None
    REDOC_URL: str = None


settings = Settings()
