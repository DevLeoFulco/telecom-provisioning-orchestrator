from uuid import uuid4

from app.application.commands import StartProvisioningCommand
from app.application.ports.provisioning_repository import ProvisioningRepository
from app.domain.provisioning import (
    Location,
    Provisioning,
    ProvisioningStatus,
)


class StartProvisioningUseCase:

    def __init__(
        self,
        repository: ProvisioningRepository
    ):
        self.repository = repository

    def execute(
        self,
        command: StartProvisioningCommand
    ) -> Provisioning:

        provisioning = Provisioning(
            provisioning_id=str(uuid4()),
            customer_id=command.customer_id,
            service_type=command.service_type,
            bandwidth=command.bandwidth,
            location=Location(
                city=command.city,
                state=command.state
            ),
            status=ProvisioningStatus.REQUESTED
        )

        return self.repository.save(provisioning)