from app.application.ports.provisioning_repository import ProvisioningRepository
from app.domain.provisioning import Provisioning


class InMemoryProvisioningRepository(ProvisioningRepository):

    def __init__(self):
        self._storage: dict[str, Provisioning] = {}

    def save(self, provisioning: Provisioning) -> Provisioning:
        self._storage[provisioning.provisioning_id] = provisioning
        return provisioning