from dataclasses import dataclass

from app.application.input.commands.check_network_availability_command import (
    CheckNetworkAvailabilityCommand,
)
from app.application.output.ports.network_inventory_gateway import (
    NetworkInventoryGateway,
)


@dataclass(frozen=True)
class CheckNetworkAvailabilityResult:
    available: bool


class CheckNetworkAvailabilityUseCase:

    def __init__(
        self,
        gateway: NetworkInventoryGateway,
    ) -> None:
        self.gateway = gateway

    async def execute(
        self,
        command: CheckNetworkAvailabilityCommand,
    ) -> CheckNetworkAvailabilityResult:

        available = await self.gateway.check_availability(
            city=command.city,
            state=command.state,
            bandwidth=command.bandwidth,
        )

        return CheckNetworkAvailabilityResult(
            available=available
        )