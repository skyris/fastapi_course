import fastapi
import fastapi_chameleon
import uvicorn

from views import account, home, packages


app = fastapi.FastAPI()

fastapi_chameleon.global_init('templates')

app.include_router(home.router)
app.include_router(account.router)
app.include_router(packages.router)


if __name__ == "__main__":
    uvicorn.run(app)
