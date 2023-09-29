FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

RUN /bin/sh -c pip install --no-cache-dir --upgrade -r requirements.txt

