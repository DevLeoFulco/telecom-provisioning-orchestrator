from dataclasses import dataclass
from enum import Enum
from app.domain.exceptions import InvalidBandwidthError


class ServiceType(str, Enum):
    FIBER = "FIBER"
    MPLS = "MPLS"
    INTERNET = "INTERNET"


class ProvisioningStatus(str, Enum):
    REQUESTED = "REQUESTED"
    VALIDATING_CUSTOMER = "VALIDATING_CUSTOMER"
    CHECKING_NETWORK = "CHECKING_NETWORK"
    RESERVING_RESOURCE = "RESERVING_RESOURCE"
    PROVISIONING = "PROVISIONING"
    ACTIVATED = "ACTIVATED"
    FAILED = "FAILED"


@dataclass(frozen=True)
class Location:
    city: str
    state: str


@dataclass
class Provisioning:
    provisioning_id: str
    customer_id: str
    service_type: ServiceType
    bandwidth: int
    location: Location
    status: ProvisioningStatus

    def __post_init__(self):
        if self.bandwidth <= 0:
            raise InvalidBandwidthError(
                "Bandwidth must be greater than zero."
            )

        if self.bandwidth > 10000:
            raise InvalidBandwidthError(
                "Bandwidth cannot exceed 10000 Mbps."
            )