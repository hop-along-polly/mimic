from fastapi import FastAPI, APIRouter

# Maybe create a function called load_routers or something that takes in the fast_api
# app and then appends all of the imported routers :shrug:
from alwayson.controllers.status import router as status_router
from alwayson.controllers.get import router as get_router
from alwayson.controllers.manifests import router as manifest_router

app = FastAPI()

# Setup AlwaysON System Routes
# The sys_router for is for Always ON System Routes
sys_router = APIRouter(prefix="/v1")

sys_router.include_router(manifest_router)
sys_router.include_router(status_router)


# Setup Echo Routes.
# The echo_router is the router that will handle all requests from a test system and echo's back the configured response
echo_router = APIRouter()
echo_router.include_router(get_router)

# Include the echo routes and system routes in the main application
app.include_router(sys_router)
app.include_router(echo_router)
