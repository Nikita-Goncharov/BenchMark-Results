import os
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
from dotenv import load_dotenv

from models import AverageBenchMarkResult
from utils import calculate_average_benchmark_result, load_benchmark_results

load_dotenv()

app = FastAPI()

DEBUG = os.getenv("SUPERBENCHMARK_DEBUG")
DEBUG = DEBUG.lower() == "true" if isinstance(DEBUG, str) else False


@app.middleware("http")
async def check_debug_mode(request: Request, call_next) -> Response:
    if DEBUG:
        response = await call_next(request)
    else:
        response = JSONResponse(content={"detail": "Feature not available yet."}, status_code=501)

    return response

# app.add_middleware(check_debug_mode)


@app.get("/results/average/", response_model=AverageBenchMarkResult)
async def get_average_results():
    results = load_benchmark_results()
    return calculate_average_benchmark_result(results)


@app.get("/results/average/{start_time}/{end_time}", response_model=AverageBenchMarkResult)
async def get_average_results_by_time_window(start_time: str, end_time: str):
    results = load_benchmark_results()
    start_datetime, end_datetime = datetime.fromisoformat(start_time), datetime.fromisoformat(end_time)

    results = list(filter(
        lambda result: start_datetime <= datetime.fromisoformat(result["timestamp"]) <= end_datetime,
        results
    ))

    return calculate_average_benchmark_result(results)
