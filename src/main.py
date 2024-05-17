import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api import router
from core import app_settings

app = FastAPI(
    title=app_settings.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)
app.include_router(router, prefix='/api')

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=app_settings.PROJECT_HOST,
        port=app_settings.PROJECT_PORT,
    )
