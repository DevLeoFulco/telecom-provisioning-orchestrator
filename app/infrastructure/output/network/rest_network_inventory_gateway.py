import httpx

from app.application.output.ports.network_inventory_gateway import (
    NetworkInventoryGateway,
)


class RestNetworkInventoryGateway(
    NetworkInventoryGateway
):

    def __init__(
        self,
        base_url: str,
    ) -> None:
        self.base_url = base_url

    async def check_availability(
        self,
        city: str,
        state: str,
        bandwidth: int,
    ) -> bool:

        async with httpx.AsyncClient(
            base_url=self.base_url
        ) as client:

            response = await client.get(
                "/api/v1/network/availability",
                params={
                    "city": city,
                    "state": state,
                    "bandwidth": bandwidth,
                },
            )

            response.raise_for_status()

            data = response.json()

            return bool(
                data["available"]
            )