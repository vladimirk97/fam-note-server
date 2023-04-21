from fastapi import APIRouter


router = APIRouter()

@router.get('/', include_in_schema = True)
def sign_in()