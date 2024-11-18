from fastapi import FastAPI, Request, Response
import uvicorn


app = FastAPI()


@app.get("/", response_class={})
async def wellcom():
    return "hello world"


if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=8000)
