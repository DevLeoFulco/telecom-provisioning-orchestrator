from fastapi import APIRouter, Depends, status

from app.api.schemas import (
    ProvisioningRequest,
    ProvisioningResponse,
)
from app.application.commands import StartProvisioningCommand
from app.application.start_provisioning import StartProvisioningUseCase
from app.infrastructure.repositories.dependencies import (
    get_start_provisioning_use_case,
)


router = APIRouter(
    prefix="/api/v1/provisionings",
    tags=["Provisioning"]
)


@router.post(
    "",
    response_model=ProvisioningResponse,
    status_code=status.HTTP_201_CREATED
)
def start_provisioning(
    request: ProvisioningRequest,
    use_case: StartProvisioningUseCase = Depends(
        get_start_provisioning_use_case
    )
) -> ProvisioningResponse:

    provisioning = use_case.execute(
        StartProvisioningCommand(
            customer_id=request.customer_id,
            service_type=request.service_type,
            bandwidth=request.bandwidth,
            city=request.location.city,
            state=request.location.state
        )
    )

    return ProvisioningResponse(
        provisioning_id=provisioning.provisioning_id,
        customer_id=provisioning.customer_id,
        service_type=provisioning.service_type,
        bandwidth=provisioning.bandwidth,
        status=provisioning.status.value
    )