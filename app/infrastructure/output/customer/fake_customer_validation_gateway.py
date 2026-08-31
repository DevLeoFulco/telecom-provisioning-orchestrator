from app.application.output.ports.customer_validation_gateway import (
    CustomerValidationGateway,
)


class FakeCustomerValidationGateway(
    CustomerValidationGateway
):

    async def is_valid(
        self,
        customer_id: str,
    ) -> bool:

        return customer_id.startswith("CUS-")