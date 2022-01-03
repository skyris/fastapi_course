import fastapi
import fastapi_chameleon
from fastapi.staticfiles import StaticFiles
import uvicorn

from views import account, home, packages


app = fastapi.FastAPI()


def main():
    configure()
    uvicorn.run(app, host='0.0.0.0', port=8000)


def configure():
    configure_routes()
    configure_templates()


def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


def configure_templates():
    fastapi_chameleon.global_init('templates')


if __name__ == "__main__":
    main()
else:
    configure()
