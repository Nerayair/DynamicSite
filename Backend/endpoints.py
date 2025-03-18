from fastapi import FastAPI
from pydantic import BaseModel

from get_gemini_response import get_gemini_response

app = FastAPI()

# Pydantic model for the request body
class PromptRequest(BaseModel):
    prompt: str

# Endpoint to receive text and return the Gemini response
@app.post("/get_gemini_response")
async def gemini_response(request: PromptRequest):
    response = get_gemini_response(request.prompt)
    return {"response": response}
