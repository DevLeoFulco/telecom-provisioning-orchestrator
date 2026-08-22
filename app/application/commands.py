from dataclasses import dataclass

from app.domain.provisioning import ServiceType


@dataclass(frozen=True)
class StartProvisioningCommand:
    customer_id: str
    service_type: ServiceType
    bandwidth: int
    city: str
    state: str