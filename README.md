# fib_api

## Overview
n番目のフィボナッチ数列の値を返すREST API

エンドポイント : https://fib-api-ad20472c44e6.herokuapp.com/

## Requirement
### OS
- macOS 13.4

### Library
- Python
  - Flask
- Docker
- docker-compose

## Usage
1. Clone this repository
```
git clone https://github.com/ogatakatsuya/fib_api.git
```
3. Build and Boot
```
docker compose up --build
```
## Features

## Request and Response

### Example
Request:
```
curl -X GET -H "Content-Type: application/json" "https://fib-api-ad20472c44e6.herokuapp.com/fib?n=99"
```

Response:
```
{
  "result": 218922995834555169026
}
```

Request:
```
curl -X GET -H "Content-Type: application/json" "https://fib-api-ad20472c44e6.herokuapp.com/fib?n=abc"
```

Response:
```
{
  "status": 400,
  "message": "Parameter n must be a number."
}
```

## Author
[Ogata Katsuya](https://github.com/ogatakatsuya)
## File structure

```
.
├── Dockerfile
├── README.md
├── app.py
├── docker-compose.yml
├── heroku.yml
├── pytest.ini
├── requirements.txt
├── .github
│   └── workflows
│       └── actions.yml
├── src
│   └── fib.py
└── test
    └── test_main.py

```
