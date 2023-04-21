from fastapi import APIRouter
from .endpoints import sign_in

api_router = APIRouter()

api_router.include_router(sign_in.router, prefix="/signin")