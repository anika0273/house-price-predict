# Base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy specific requirements for the frontend and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the frontend source code
COPY frontend/ /app

# Default API URL (can be overridden at runtime)
ENV API_URL=http://backend:8000

# Expose the port your Streamlit app listens on
EXPOSE 8501

# Command to run your Streamlit application
#CMD ["streamlit", "run", "frontend.py", "--server.port=8501", "--server.enableCORS=false"]

# Run Streamlit and bind API URL dynamically
#CMD ["sh", "-c", "streamlit run frontend.py --server.port=8501 --server.enableCORS=false"]
CMD ["sh", "-c", "streamlit run frontend.py --server.port=${PORT} --server.address=0.0.0.0 --server.enableCORS=false --server.enableXsrfProtection=false"]
