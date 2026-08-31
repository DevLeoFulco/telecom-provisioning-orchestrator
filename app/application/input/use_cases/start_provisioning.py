from app.application.input.commands.start_provisioning_command import (
    StartProvisioningCommand,
)
from app.application.output.ports.provisioning_repository import (
    ProvisioningRepository,
)
from app.domain.provisioning import Provisioning


class StartProvisioningUseCase:

    def __init__(
        self,
        repository: ProvisioningRepository
    ) -> None:
        self.repository = repository

    async def execute(
        self,
        command: StartProvisioningCommand
    ) -> Provisioning:

        provisioning = Provisioning(
            customer_id=command.customer_id,
            service_type=command.service_type,
            bandwidth=command.bandwidth,
            city=command.city,
            state=command.state,
        )

        return await self.repository.save(
            provisioning
        )