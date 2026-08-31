from app.application.output.ports.provisioning_repository import (
    ProvisioningRepository,
)
from app.domain.provisioning import Provisioning


class FakeProvisioningRepository(
    ProvisioningRepository
):
    def __init__(self) -> None:
        self.saved: list[Provisioning] = []

    async def save(
        self,
        provisioning: Provisioning
    ) -> Provisioning:
        self.saved.append(provisioning)
        return provisioning