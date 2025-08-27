# Use Python 3.12 as base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome for Testing (more reliable method)
RUN curl -fsSL https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json | \
    grep -oE '"version":"[^"]*' | head -1 | cut -d'"' -f4 > /tmp/chrome_version.txt \
    && CHROME_VERSION=$(cat /tmp/chrome_version.txt) \
    && wget -O /tmp/chrome-linux64.zip "https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chrome-linux64.zip" \
    && wget -O /tmp/chromedriver-linux64.zip "https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chromedriver-linux64.zip" \
    && unzip /tmp/chrome-linux64.zip -d /opt/ \
    && unzip /tmp/chromedriver-linux64.zip -d /opt/ \
    && ln -sf /opt/chrome-linux64/chrome /usr/local/bin/chrome \
    && ln -sf /opt/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chrome /usr/local/bin/chromedriver \
    && rm -f /tmp/chrome-linux64.zip /tmp/chromedriver-linux64.zip /tmp/chrome_version.txt

# Set work directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create a non-root user
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Expose port for health checks (Railway requirement)
EXPOSE 8080

# Command to run the application
CMD ["python", "main.py"]