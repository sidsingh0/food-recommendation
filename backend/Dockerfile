FROM python:3.11

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt
  
# Copy the rest of the backend files
COPY . /app/

# Expose port 5000
EXPOSE 5000

# Start the app
CMD ["waitress-serve", "--listen=*:5000", "app:app"]