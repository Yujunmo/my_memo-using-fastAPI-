from fastapi import *
from fastapi.templating import Jinja2Templates
from database.connection import get_db
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()
templates = Jinja2Templates(directory="templates")