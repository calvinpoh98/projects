# Use an official Python runtime as a parent image
FROM python:3.8-slim
WORKDIR /app

# Copy only the requirements.txt file to use Docker's caching mechanism
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code
COPY . /app

# Make port 80 available
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "./app.py"]
