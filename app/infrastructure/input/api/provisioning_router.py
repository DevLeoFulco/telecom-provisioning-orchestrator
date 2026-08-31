from fastapi import APIRouter, Depends, status

from app.application.input.commands.start_provisioning_command import (
    StartProvisioningCommand,
)
from app.application.input.use_cases.start_provisioning import (
    StartProvisioningUseCase,
)
from app.dependencies import (
    get_start_provisioning_use_case,
)
from app.infrastructure.input.api.schemas import (
    ProvisioningResponse,
    StartProvisioningRequest,
)


router = APIRouter(
    prefix="/api/v1/provisionings",
    tags=["Provisioning"],
)


@router.post(
    "",
    response_model=ProvisioningResponse,
    status_code=status.HTTP_201_CREATED,
)
async def start_provisioning(
    request: StartProvisioningRequest,
    use_case: StartProvisioningUseCase = Depends(
        get_start_provisioning_use_case
    ),
) -> ProvisioningResponse:

    command = StartProvisioningCommand(
        customer_id=request.customer_id,
        service_type=request.service_type,
        bandwidth=request.bandwidth,
        city=request.location.city,
        state=request.location.state,
    )

    provisioning = await use_case.execute(
        command
    )

    return ProvisioningResponse(
        customer_id=provisioning.customer_id,
        service_type=provisioning.service_type,
        bandwidth=provisioning.bandwidth,
        city=provisioning.city,
        state=provisioning.state,
        status=provisioning.status.value,
    )