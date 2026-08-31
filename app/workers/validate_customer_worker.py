import asyncio

from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ConnectedJobContext,
    WorkerConfig,
)


async def validate_customer(
    job: ConnectedJobContext
) -> dict[str, object]:

    variables = job.variables.to_dict()

    customer_id = variables.get("customer_id")

    print(
        f"[validate-customer] "
        f"Validando cliente: {customer_id}"
    )

    return {
        "customer_valid": True
    }


async def main() -> None:

    async with CamundaAsyncClient() as client:

        config = WorkerConfig(
            job_type="validate-customer",
            job_timeout_milliseconds=30_000,
            worker_name="telecom-validate-customer-worker"
        )

        client.create_job_worker(
            config=config,
            callback=validate_customer
        )

        print(
            "Worker validate-customer aguardando jobs..."
        )

        await client.run_workers()


if __name__ == "__main__":
    asyncio.run(main())