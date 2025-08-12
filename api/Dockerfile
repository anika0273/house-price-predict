# Base image
FROM python:3.11-slim


# Set working directory inside the container
WORKDIR /app

# Copy specific requirements for the backend and install them

# Copy requirements.txt to the working directory or Container
COPY requirements.txt . 
# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the models folder to the working directory of the container i.e. /app folder
COPY api/ /app/
# COPY models/ /app/models/ # uploaded the joblib file to google cloud directly

# Create models directory (model will be downloaded at runtime)
RUN mkdir -p /app/models

# Expose the port your FastAPI app listens on
EXPOSE 8080

# Command to run your FastAPI application
#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["python", "app.py"]
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]

# Starts the FastAPI app: "app" is the filename (app.py), and second "app" is the FastAPI object