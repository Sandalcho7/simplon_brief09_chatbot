FROM python:3.11-alpine

WORKDIR /app

# Copy source code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable during build
ENV EDEN_KEY=$EDEN_AI_KEY

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]