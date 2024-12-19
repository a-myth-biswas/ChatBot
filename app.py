from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, File, HTTPException
from pydantic import BaseModel
from main import main_function
import uvicorn


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

class QueryRequest(BaseModel):
    query : str

@app.post("/query")
async def chatbot(request : QueryRequest):
    try:
        query = request.query.strip()
        if not query:
            raise HTTPException(status_code=400, detail="Query can not be empty")
        answer = main_function(query)
        return{"question":query, "answer":answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = "8503")