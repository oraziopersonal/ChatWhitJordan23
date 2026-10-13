from fastapi import FastAPI

app = FastAPI(title="ChatWithJames API")


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)