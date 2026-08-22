from pydantic import BaseModel, Field

from app.domain.provisioning import ServiceType


class LocationRequest(BaseModel):
    city: str = Field(min_length=2, max_length=100)
    state: str = Field(min_length=2, max_length=2)


class ProvisioningRequest(BaseModel):
    customer_id: str = Field(min_length=3, max_length=50)
    service_type: ServiceType
    bandwidth: int = Field(gt=0, le=10000)
    location: LocationRequest


class ProvisioningResponse(BaseModel):
    provisioning_id: str
    customer_id: str
    service_type: ServiceType
    bandwidth: int
    status: str