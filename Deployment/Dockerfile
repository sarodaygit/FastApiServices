# Use minimal Python base image
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Copy source code and requirements
COPY Sources/FastApiServices /app/FastApiServices
COPY Sources/requirements.txt /app

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set environment variables (defaults, can be overridden via docker run)
ENV PYTHONPATH=/app/FastApiServices
ENV ENV=dev
ENV MONGO_CERT_PATH=/certs/ca.pem

# Run the FastAPI app with Uvicorn (with reload for dev)
CMD ["uvicorn", "FastApiServices.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
