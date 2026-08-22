from app.application.start_provisioning import StartProvisioningUseCase
from app.infrastructure.repositories.in_memory_provisioning_repository import (
    InMemoryProvisioningRepository,
)


provisioning_repository = InMemoryProvisioningRepository()


def get_start_provisioning_use_case() -> StartProvisioningUseCase:
    return StartProvisioningUseCase(
        repository=provisioning_repository
    )