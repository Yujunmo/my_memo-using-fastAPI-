from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import JSONResponse
from api.login_api import router as login_router
from api.memo_api import router as memo_router
from api.common import templates
from database.orm import app_lifespan

app = FastAPI(lifespan=app_lifespan, docs_url=None, redoc_url=None)
app.add_middleware(SessionMiddleware,secret_key="your_key")
app.include_router(login_router)
app.include_router(memo_router)

@app.get("/")
async def home(request : Request):
    return templates.TemplateResponse('home.html',{"request":request})

@app.get("/about", response_class=JSONResponse)
async def about():
    return {"message":"this is my memo application"}

