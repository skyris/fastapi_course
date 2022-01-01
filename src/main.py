import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get('/')
def index():
    content = """
    <h1>Hello FastAPI Web App</h1>
    <div>This is where our fake pypi app will live!</div>
    """
    resp = fastapi.responses.HTMLResponse(content)
    return resp


if __name__ == "__main__":
    uvicorn.run(app)
