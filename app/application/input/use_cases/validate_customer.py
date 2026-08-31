from dataclasses import dataclass

from app.application.input.commands.validate_customer_command import (
    ValidateCustomerCommand,
)
from app.application.output.ports.customer_validation_gateway import (
    CustomerValidationGateway,
)


@dataclass(frozen=True)
class ValidateCustomerResult:
    customer_id: str
    valid: bool


class ValidateCustomerUseCase:

    def __init__(
        self,
        gateway: CustomerValidationGateway,
    ) -> None:
        self.gateway = gateway

    async def execute(
        self,
        command: ValidateCustomerCommand,
    ) -> ValidateCustomerResult:

        valid = await self.gateway.is_valid(
            command.customer_id
        )

        return ValidateCustomerResult(
            customer_id=command.customer_id,
            valid=valid,
        )