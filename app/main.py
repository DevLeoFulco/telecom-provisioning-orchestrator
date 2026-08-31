from fastapi import FastAPI

from app.infrastructure.input.api.provisioning_router import (
    router as provisioning_router,
)


app = FastAPI(
    title="Telecom Provisioning Orchestrator",
    version="1.0.0",
)


app.include_router(
    provisioning_router
)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "UP"
    }