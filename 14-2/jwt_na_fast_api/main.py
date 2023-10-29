import redis.asyncio as redis_go
import uvicorn 

from fastapi import FastAPI
from fastapi_limiter import FastAPILimiter

from jwt_na_fast_api.routes import contacts_book, auth, users
from jwt_na_fast_api.conf.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [ 
    "http://localhost:3000"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix='/api')
app.include_router(contacts_book.router, prefix='/api')
app.include_router(users.router, prefix='/api')


@app.on_event("startup")
async def startup():
    """
    The startup function is called when the application starts up.
    It's a good place to initialize things that are needed by your app, such as database connections.
    
    :return: A list of coroutines
    :doc-author: Trelent
    """
    r = await redis_go.Redis(host='localhost', port= settings.redis_port, db=0, encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(r)

@app.get("/", name='project start page')
def read_root():
    """
    The read_root function returns a dictionary with the key &quot;message&quot; and value &quot;Hello World&quot;.
    
    
    :return: A dictionary
    :doc-author: Trelent
    """
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True)
