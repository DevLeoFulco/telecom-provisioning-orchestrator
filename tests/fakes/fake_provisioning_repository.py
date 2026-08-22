from app.application.ports.provisioning_repository import ProvisioningRepository
from app.domain.provisioning import Provisioning


class FakeProvisioningRepository(ProvisioningRepository):

    def __init__(self):
        self.saved_provisioning: Provisioning | None = None

    def save(self, provisioning: Provisioning) -> Provisioning:
        self.saved_provisioning = provisioning
        return provisioning