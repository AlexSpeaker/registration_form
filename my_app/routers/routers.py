from typing import Tuple

from fastapi import APIRouter
from routers.auth.route import auth_router

routers: Tuple[APIRouter] = (auth_router,)
