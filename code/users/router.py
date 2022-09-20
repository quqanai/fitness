from fastapi import APIRouter

from .handlers import register

router = APIRouter()
router.add_api_route('/register', register, methods=['POST'])
