from fastapi import FastAPI
from fast_api_app.routes import contacts_book

app = FastAPI()

app.include_router(contacts_book.router, prefix='/api')

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

