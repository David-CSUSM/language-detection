FROM python:3.10

WORKDIR /language-detection

COPY ./requirements.txt /language-detection/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /language-detection/requirements.txt

COPY ./app /language-detection/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
