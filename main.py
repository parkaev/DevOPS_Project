from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Корневой endpoint, возвращает приветствие."""
    return {"message": "Hello, World! This is a FastAPI app."}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """Endpoint для получения информации о item по ID."""
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)