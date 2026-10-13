import logging
import os

from fastapi import FastAPI, HTTPException
from openai import OpenAI, OpenAIError
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="ChatWithJames API", version="1.0.0")


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}


@app.get("/square/{number}")
async def square(number: int) -> dict[str, int]:
    return {"number": number, "square": number * number}


@app.post("/chat")
def chat(request: ChatRequest) -> dict[str, str]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="Server is missing the OPENAI_API_KEY environment variable.",
        )

    client = OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": request.message}],
        )
    except OpenAIError as exc:
        logger.exception("OpenAI chat request failed")
        raise HTTPException(
            status_code=502,
            detail="The request to the OpenAI service failed.",
        ) from exc

    answer = response.choices[0].message.content if response.choices else None
    if answer is None:
        raise HTTPException(
            status_code=502,
            detail="The OpenAI service returned no answer.",
        )
    return {"response": answer}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
