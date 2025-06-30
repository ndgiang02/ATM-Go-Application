# Dockerfile

# 1. Base image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy project files
COPY . .

# 5. Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 6. Expose port
EXPOSE 8000

# 7. Default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]