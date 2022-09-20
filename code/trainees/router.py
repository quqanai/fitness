from fastapi import APIRouter

from .handlers import create, get_all


router = APIRouter()
router.add_api_route('/', create, methods=['POST'])
router.add_api_route('/', get_all, methods=['GET'])
