FROM python:3.10-slim
RUN python -m pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN pip install pytest
CMD ["python", "app.py"]
