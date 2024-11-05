#py base image
FROM python:3.9-slim

#working directory
WORKDIR /app

# copy project files
COPY . .

#dependencies
RUN pip install -r requirements.txt

# Run application
CMD ["python", "-m", "app.main"]
