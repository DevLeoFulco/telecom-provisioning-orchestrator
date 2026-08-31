import pytest

from app.application.input.commands.start_provisioning_command import (
    StartProvisioningCommand,
)
from app.application.input.use_cases.start_provisioning import (
    StartProvisioningUseCase,
)
from app.domain.exceptions import (
    InvalidBandwidthError,
)
from app.domain.provisioning import (
    ProvisioningStatus,
    ServiceType,
)
from tests.fakes.fake_provisioning_repository import (
    FakeProvisioningRepository,
)


@pytest.mark.asyncio
async def test_should_start_provisioning() -> None:
    repository = FakeProvisioningRepository()

    use_case = StartProvisioningUseCase(
        repository=repository
    )

    command = StartProvisioningCommand(
        customer_id="CUS-12345",
        service_type=ServiceType.FIBER,
        bandwidth=500,
        city="Recife",
        state="PE",
    )

    result = await use_case.execute(command)

    assert result.customer_id == "CUS-12345"
    assert result.service_type == ServiceType.FIBER
    assert result.bandwidth == 500
    assert result.city == "Recife"
    assert result.state == "PE"
    assert result.status == ProvisioningStatus.PENDING

    assert len(repository.saved) == 1
    assert repository.saved[0] == result


@pytest.mark.asyncio
async def test_should_reject_invalid_bandwidth() -> None:
    repository = FakeProvisioningRepository()

    use_case = StartProvisioningUseCase(
        repository=repository
    )

    command = StartProvisioningCommand(
        customer_id="CUS-12345",
        service_type=ServiceType.FIBER,
        bandwidth=0,
        city="Recife",
        state="PE",
    )

    with pytest.raises(InvalidBandwidthError):
        await use_case.execute(command)

    assert len(repository.saved) == 0