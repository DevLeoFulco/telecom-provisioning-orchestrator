from app.application.input.use_cases.start_provisioning import (
    StartProvisioningUseCase,
)
from app.infrastructure.output.repositories.in_memory_provisioning_repository import (
    InMemoryProvisioningRepository,
)

from app.application.input.use_cases.validate_customer import (
    ValidateCustomerUseCase,
)
from app.infrastructure.output.customer.fake_customer_validation_gateway import (
    FakeCustomerValidationGateway,
)


provisioning_repository = InMemoryProvisioningRepository()
customer_validation_gateway = FakeCustomerValidationGateway()

def get_start_provisioning_use_case() -> StartProvisioningUseCase:
    return StartProvisioningUseCase(
        repository=provisioning_repository
    )

def get_validate_customer_use_case() -> ValidateCustomerUseCase:
    return ValidateCustomerUseCase(
        gateway=customer_validation_gateway
    )