from dataclasses import dataclass


@dataclass(frozen=True)
class StartProvisioningCommand:
    customer_id: str
    service_type: str
    bandwidth: int
    city: str
    state: str