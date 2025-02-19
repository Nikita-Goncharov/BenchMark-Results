from typing_extensions import TypedDict


class BenchMarkResult(TypedDict):
    request_id: str
    prompt_text: str
    generated_text: str
    token_count: int
    time_to_first_token: int
    time_per_output_token: int
    total_generation_time: int
    timestamp: str


class AverageBenchMarkResult(TypedDict):
    average_token_count: float
    average_time_to_first_token: float
    average_time_per_output_token: float
    average_total_generation_time: float
