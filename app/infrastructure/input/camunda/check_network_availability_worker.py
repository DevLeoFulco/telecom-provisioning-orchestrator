import asyncio

from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ConnectedJobContext,
    WorkerConfig,
)

from app.application.input.commands.check_network_availability_command import (
    CheckNetworkAvailabilityCommand,
)
from app.dependencies import (
    get_check_network_availability_use_case,
)


async def check_network_availability(
    job: ConnectedJobContext,
) -> dict[str, object]:

    variables = job.variables.to_dict()

    city = variables.get("city")
    state = variables.get("state")
    bandwidth = variables.get("bandwidth")

    use_case = get_check_network_availability_use_case()

    result = await use_case.execute(
        CheckNetworkAvailabilityCommand(
            city=city,
            state=state,
            bandwidth=bandwidth,
        )
    )

    print(
        f"[check-network-availability] "
        f"city={city} "
        f"state={state} "
        f"bandwidth={bandwidth} "
        f"available={result.available}"
    )

    return {
        "network_available": result.available
    }


async def main() -> None:

    async with CamundaAsyncClient() as client:

        config = WorkerConfig(
            job_type="check-network-availability",
            job_timeout_milliseconds=30_000,
            worker_name="telecom-check-network-worker",
        )

        client.create_job_worker(
            config=config,
            callback=check_network_availability,
        )

        print(
            "Worker check-network-availability aguardando jobs..."
        )

        await client.run_workers()


if __name__ == "__main__":
    asyncio.run(main())