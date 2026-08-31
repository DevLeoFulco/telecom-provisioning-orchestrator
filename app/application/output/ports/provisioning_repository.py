from abc import ABC, abstractmethod

from app.domain.provisioning import Provisioning


class ProvisioningRepository(ABC):

    @abstractmethod
    async def save(
        self,
        provisioning: Provisioning
    ) -> Provisioning:
        raise NotImplementedError