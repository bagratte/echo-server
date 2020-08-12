FROM python:3.8

WORKDIR /app
COPY requirements.txt .
RUN pip install --requirement requirements.txt

COPY . .
ENV FLASK_APP=http-echo.py
EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
