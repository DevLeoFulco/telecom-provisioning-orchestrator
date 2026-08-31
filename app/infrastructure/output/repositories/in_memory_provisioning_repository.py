from app.application.output.ports.provisioning_repository import (
    ProvisioningRepository,
)
from app.domain.provisioning import Provisioning


class InMemoryProvisioningRepository(ProvisioningRepository):

    def __init__(self) -> None:
        self._provisionings: list[Provisioning] = []

    async def save(
        self,
        provisioning: Provisioning
    ) -> Provisioning:

        self._provisionings.append(provisioning)

        return provisioning