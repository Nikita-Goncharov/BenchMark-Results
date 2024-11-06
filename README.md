# BenchMark average results app
***
Created with FastAPI

## Setup
* Clone repo:
```bash
$ git clone https://github.com/Nikita-Goncharov/BenchMark-Results.git  
```

* Create virtualenvironment and activate it:
```bash
$ python -m venv env
$ . env/bin/activate
```

* Install requirements:
```bash
$ pip install -r requirements.txt 
```

* Make **.env** file in project dir with content:
```
SUPERBENCHMARK_DEBUG=True
```
* Make **test_database.json** file in project dir with content:
```
{
	"benchmarking_results": [
		{
			"request_id": str,
			"prompt_text": str,
			"generated_text": str,
			"token_count": int,
			"time_to_first_token": int,
			"time_per_output_token": int,
			"total_generation_time": int,
			"timestamp": str
		},
		...
	]
}
```
* Dev start server:
```bash
$ fastapi dev main.py
```

## Ruff linter and formatter checking:
```bash
$ ruff check
$ ruff format
```
