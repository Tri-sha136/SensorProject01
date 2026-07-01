FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app:
    COPY prediction_artifacts/ /app/artifacts/

RUN pip install -r requirements.txt
CMD ["python3","app.py"]