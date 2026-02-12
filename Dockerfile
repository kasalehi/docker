FROM python:3-slim
workdir /app
copy . .
run pip install -r requirements.txt
cmd ["python", "app.py"]
expose 5000