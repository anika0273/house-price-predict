# Base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy specific requirements for the frontend and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the frontend source code
COPY frontend/ /app

# Expose the port your Streamlit app listens on
EXPOSE 8501

# Command to run your Streamlit application
CMD ["streamlit", "run", "frontend.py", "--server.port=8501", "--server.enableCORS=false"]
