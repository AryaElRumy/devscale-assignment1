from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.routes.students import students_router
from app.setting import settings

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    docs_url=settings.DOC_URL,
    redoc_url=settings.REDOC_URL,
)

app.include_router(students_router)


@app.get("/")
def hello():
    return {"Mochamad Arya El Rumy - Assignment 1"}


@app.get("/health")
async def health_check():
    return {"health": "ok"}


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    if app.openapi_url is None:
        raise ValueError("no openapi url")
    return get_scalar_api_reference(openapi_url=app.openapi_url, title=app.title)
