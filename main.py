from fastapi import FastAPI
from routes import router as api_router
from config import log_request

app = FastAPI()

app.include_router(api_router)

@app.middleware("http")
async def middleware(request, call_next):
    """
    Middleware function to log HTTP requests.

    Parameters:
        request: Incoming HTTP request.
        call_next: The function to call to continue processing the request.

    Returns:
        HTTP response to the request.
    """
    response = await log_request(request, call_next)
    return response