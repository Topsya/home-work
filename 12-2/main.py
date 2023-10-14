

from fastapi import FastAPI

from jwt_na_fast_api.routes import contacts_book, auth

app = FastAPI()

app.include_router(auth.router, prefix='/api')
app.include_router(contacts_book.router, prefix='/api')

@app.get("/")
def read_root():
    return {"message": "Hello World"}


