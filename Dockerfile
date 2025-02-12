# Use the official Python image from the Docker Hub
FROM python:3.9.17-bookworm

# Define environment variable
ENV NAME World

ENV PYTHONUMBUFFERED True

ENV APP_HOME /back-end
WORKDIR $APP_HOME
COPY . ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# expose to port 8080
EXPOSE 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app


