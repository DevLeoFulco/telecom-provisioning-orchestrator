from dataclasses import dataclass


@dataclass(frozen=True)
class CheckNetworkAvailabilityCommand:
    city: str
    state: str
    bandwidth: int