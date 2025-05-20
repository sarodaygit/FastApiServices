# Use the Python 3.8 image as the base
FROM python:3.8

# Set the working directory inside the container to /code
WORKDIR /code

# Copy the requirements.txt file from the Sources directory on the host machine to the /code directory inside the container
COPY Sources/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY Sources /code/Sources

# Make port 80 available to the world outside this container
EXPOSE 8004

# Define environment variable to include the Sources directory in PYTHONPATH
ENV PYTHONPATH=/code/Sources/FastApiServices

# Run uvicorn server with the app instance from main module
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8004"]
