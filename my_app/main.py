from core.factory_function import get_app
from routers.routers import routers
from settings.app_settings import settings

app = get_app(settings=settings, routers_sequence=routers)
