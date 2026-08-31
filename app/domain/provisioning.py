from dataclasses import dataclass
from enum import Enum

from app.domain.exceptions import (
    InvalidBandwidthError,
    InvalidCustomerIdError,
    InvalidLocationError,
    InvalidServiceTypeError,
)


class ServiceType(str, Enum):
    FIBER = "FIBER"
    MOBILE = "MOBILE"
    BROADBAND = "BROADBAND"


class ProvisioningStatus(str, Enum):
    PENDING = "PENDING"
    VALIDATING_CUSTOMER = "VALIDATING_CUSTOMER"
    CHECKING_NETWORK = "CHECKING_NETWORK"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


@dataclass
class Provisioning:
    customer_id: str
    service_type: ServiceType
    bandwidth: int
    city: str
    state: str
    status: ProvisioningStatus = ProvisioningStatus.PENDING

    def __post_init__(self) -> None:
        self._validate_customer_id()
        self._validate_service_type()
        self._validate_bandwidth()
        self._validate_location()

    def _validate_customer_id(self) -> None:
        if not self.customer_id or len(self.customer_id.strip()) < 3:
            raise InvalidCustomerIdError(
                "customer_id deve possuir pelo menos 3 caracteres."
            )

    def _validate_service_type(self) -> None:
        if not isinstance(self.service_type, ServiceType):
            raise InvalidServiceTypeError(
                "service_type inválido."
            )

    def _validate_bandwidth(self) -> None:
        if self.bandwidth <= 0:
            raise InvalidBandwidthError(
                "bandwidth deve ser maior que zero."
            )

    def _validate_location(self) -> None:
        if not self.city or len(self.city.strip()) < 2:
            raise InvalidLocationError(
                "city deve possuir pelo menos 2 caracteres."
            )

        if not self.state or len(self.state.strip()) != 2:
            raise InvalidLocationError(
                "state deve possuir exatamente 2 caracteres."
            )