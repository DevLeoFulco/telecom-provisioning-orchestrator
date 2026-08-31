from abc import ABC, abstractmethod


class CustomerValidationGateway(ABC):

    @abstractmethod
    async def is_valid(
        self,
        customer_id: str,
    ) -> bool:
        raise NotImplementedError