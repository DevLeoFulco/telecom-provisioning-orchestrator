from abc import ABC, abstractmethod


class NetworkInventoryGateway(ABC):

    @abstractmethod
    async def check_availability(
        self,
        city: str,
        state: str,
        bandwidth: int,
    ) -> bool:
        raise NotImplementedError