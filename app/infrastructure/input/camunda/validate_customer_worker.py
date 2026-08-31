import asyncio

from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ConnectedJobContext,
    WorkerConfig,
)

from app.application.input.commands.validate_customer_command import (
    ValidateCustomerCommand,
)
from app.dependencies import (
    get_validate_customer_use_case,
)


async def validate_customer(
    job: ConnectedJobContext,
) -> dict[str, object]:

    variables = job.variables.to_dict()

    customer_id = variables.get("customer_id")

    use_case = get_validate_customer_use_case()

    result = await use_case.execute(
        ValidateCustomerCommand(
            customer_id=customer_id,
        )
    )

    print(
        f"[validate-customer] "
        f"customer={result.customer_id} "
        f"valid={result.valid}"
    )

    return {
        "customer_valid": result.valid
    }


async def main() -> None:

    async with CamundaAsyncClient() as client:

        config = WorkerConfig(
            job_type="validate-customer",
            job_timeout_milliseconds=30_000,
            worker_name="telecom-validate-customer-worker",
        )

        client.create_job_worker(
            config=config,
            callback=validate_customer,
        )

        print(
            "Worker validate-customer aguardando jobs..."
        )

        await client.run_workers()


if __name__ == "__main__":
    asyncio.run(main())