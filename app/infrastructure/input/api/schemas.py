from pydantic import BaseModel, Field

from app.domain.provisioning import ServiceType


class LocationRequest(BaseModel):
    city: str = Field(
        min_length=2,
        examples=["Recife"],
    )
    state: str = Field(
        min_length=2,
        max_length=2,
        examples=["PE"],
    )


class StartProvisioningRequest(BaseModel):
    customer_id: str = Field(
        min_length=3,
        examples=["CUS-12345"],
    )
    service_type: ServiceType
    bandwidth: int = Field(
        gt=0,
        examples=[500],
    )
    location: LocationRequest


class ProvisioningResponse(BaseModel):
    customer_id: str
    service_type: ServiceType
    bandwidth: int
    city: str
    state: str
    status: str