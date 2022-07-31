# Evaluate FastAPI vs Tornado Performance

A quick evaluation on FastAPI and Tornado performance to help me determine what should be used as YIS backend.

## Running servers

FastAPI single process:

    python -m uvicorn test_fastapi:app --log-level critical

FastAPI 4 processes:

    python -m uvicorn --workers 4 test_fastapi:app --log-level critical

FastAPI outputs:
```bash
$ curl -s http://localhost:8000/
"Hello world"
$ curl -s http://localhost:8000/items/123\?q\=hello |jq
{
  "item_id": 123,
  "q": "hello"
}
```

Tornado single process:

    python test_tornado.py

Tornado 4 processes:

    python test_tornado.py 1

Tornado outputs:
```bash
$ curl -s http://localhost:8888/
Hello, world
$ curl -s http://localhost:8888/items/123\?q\=hello |jq
{
  "item_id": "123",
  "q": "hello"
}
```

## Benchmarking Results

| type                    | run command                                               | result   |
| ----------------------- | --------------------------------------------------------- | -------- |
| FastAPI single process: | ab -n 10000 -c 10 http://localhost:8000/                  | 1715 rps |
| FastAPI 4 process:      | ab -n 10000 -c 10 http://localhost:8000/                  | 4100 rps |
| FastAPI single process: | ab -n 10000 -c 10 http://localhost:8000/items/123?q=hello | 1680 rps |
| FastAPI 4 process:      | ab -n 10000 -c 10 http://localhost:8000/items/123?q=hello | 3800 rps |
| Tornado single process: | ab -n 10000 -c 10 http://localhost:8888/                  | 3000 rps |
| Tornado 4 process:      | ab -n 10000 -c 10 http://localhost:8888/                  | 9000 rps |
| Tornado single process: | ab -n 10000 -c 10 http://localhost:8888/items/123?q=hello | 2800 rps |
| Tornado 4 process:      | ab -n 10000 -c 10 http://localhost:8888/items/123?q=hello | 7700 rps |

## Environments

Core i7-7700k, Ubuntu 20.04 under Windows WSL2, Python 3.10.5

