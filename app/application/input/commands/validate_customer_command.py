from dataclasses import dataclass


@dataclass(frozen=True)
class ValidateCustomerCommand:
    customer_id: str