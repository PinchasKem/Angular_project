from fastapi import FastAPI
import sqlalchemy
import uvicorn


app = FastAPI()


@app.get("/")
async def welcome():
    return {"hello": "hello world"}


if __name__ == "__main__":
    uvicorn.run(app=app, host="localhost", port=8000)
