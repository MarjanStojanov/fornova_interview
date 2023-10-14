from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse


def _include_routers(app):
    from hotel_routes import hotel_router
    app.include_router(hotel_router, prefix="/hotels", tags=["hotels"])

    return  app


def _register_healthcheck(app):
    @app.get("/ping")
    async def ping():
        return "pong"

    return app


def _register_errorhandlers(app):
    @app.exception_handler(HTTPException)
    def handle_http_exceptions(request, exc: HTTPException):
        return JSONResponse(
            content={"error": exc.detail},
            status_code=exc.status_code,
        )

    @app.exception_handler(Exception)
    def handle_uncaught_exceptions(request, exc: Exception):
        return JSONResponse(
            content={"error": "Internal Server Error"},
            status_code=500,
        )

    return app



def create_app() -> FastAPI:
    app = FastAPI()

    app = _include_routers(app)
    app = _register_healthcheck(app)
    app = _register_errorhandlers(app)

    return app


app = create_app()
