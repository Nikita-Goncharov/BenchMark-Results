import json

from models import AverageBenchMarkResult, BenchMarkResult


def calculate_average_benchmark_result(results: list[BenchMarkResult]) -> AverageBenchMarkResult:
    count = len(results)
    if count == 0:
        return AverageBenchMarkResult(
            average_token_count=0,
            average_time_per_output_token=0,
            average_time_to_first_token=0,
            average_total_generation_time=0
        )

    return AverageBenchMarkResult(
        average_token_count=sum([result["token_count"] for result in results]) / count,
        average_time_per_output_token=sum([result["time_per_output_token"] for result in results]) / count,
        average_time_to_first_token=sum([result["time_to_first_token"] for result in results]) / count,
        average_total_generation_time=sum([result["total_generation_time"] for result in results]) / count,
    )


def load_benchmark_results() -> list[BenchMarkResult] | None:
    try:
        with open("test_database.json") as file:
            json_data = json.loads(file.read())
            return json_data["benchmarking_results"]
    except Exception as ex:
        return None
