import pytest

from app.application.commands import StartProvisioningCommand
from app.application.start_provisioning import StartProvisioningUseCase
from app.domain.provisioning import (
    ProvisioningStatus,
    ServiceType,
)
from tests.fakes.fake_provisioning_repository import (
    FakeProvisioningRepository,
)
from app.domain.exceptions import InvalidBandwidthError


def test_should_start_provisioning():
    repository = FakeProvisioningRepository()

    use_case = StartProvisioningUseCase(
        repository=repository
    )

    command = StartProvisioningCommand(
        customer_id="CUS-12345",
        service_type=ServiceType.FIBER,
        bandwidth=500,
        city="Recife",
        state="PE"
    )

    result = use_case.execute(command)

    assert result.customer_id == "CUS-12345"
    assert result.service_type == ServiceType.FIBER
    assert result.bandwidth == 500
    assert result.status == ProvisioningStatus.REQUESTED

    assert repository.saved_provisioning == result

def test_should_reject_invalid_bandwidth():
    repository = FakeProvisioningRepository()

    use_case = StartProvisioningUseCase(
        repository=repository
    )

    command = StartProvisioningCommand(
        customer_id="CUS-12345",
        service_type=ServiceType.FIBER,
        bandwidth=15000,
        city="Recife",
        state="PE"
    )

    with pytest.raises(InvalidBandwidthError):
        use_case.execute(command)