FROM python:3.8-slim-buster
WORKDIR /app

# 1. First, copy the entire project directory into the container
COPY . /app

# 2. Next, explicitly map the prediction artifacts folder to the name the code expects
COPY prediction_artifacts/ /app/artifacts/

# 3. Now run your dependencies install step
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]