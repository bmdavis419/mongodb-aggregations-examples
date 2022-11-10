### Golang aggregate example

#### what the data looks like:

```
{
    "name": string,
    "midterm 1": number,
    "midterm 2": number,
    "final 1": number,
    "final 2": number,
    "section": "morning" | "online" | "evening"
}
```

#### what are we doing to do?

This aggregation will be finding the three students with the highest average score across all 4 tests.

#### to run this program

YOU NEED MONGODB DOWNLOADED AND RUNNING ON 27017 FOR THIS TO WORK!!!

THE DATA SEED IS IN THE PYTHON EXAMPLE

1. `poetry shell`
2. `poetry install`
3. `poetry run python seed/seed.py`
4. `poetry run python python_example/main.py`
