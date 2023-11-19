from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from settings import AppSettings, get_settings

from . import role

_routers = [
    role.router,
]


def create_app() -> FastAPI:
    app_settings = get_settings(AppSettings)
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=app_settings.allow_origins,
        allow_origin_regex=app_settings.allow_origin_regex,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    for router in _routers:
        app.include_router(router=router)

    @app.get("/health")
    async def healthcheck() -> None:
        return None

    @app.get("/")
    async def hello_world() -> dict[str, str]:
        return {"msg": "hello_world"}

    return app
