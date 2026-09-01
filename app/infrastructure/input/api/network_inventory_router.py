from fastapi import APIRouter


router = APIRouter(
    prefix="/api/v1/network",
    tags=["Network Inventory"],
)


@router.get("/availability")
async def check_availability(
    city: str,
    state: str,
    bandwidth: int,
) -> dict[str, object]:

    available = (
        city.strip().lower() == "recife"
        and state.strip().upper() == "PE"
        and bandwidth <= 1000
    )

    return {
        "available": available,
        "city": city,
        "state": state,
        "bandwidth": bandwidth,
    }