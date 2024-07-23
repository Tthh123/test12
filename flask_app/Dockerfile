# flask_app/Dockerfile
FROM python:3.8-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y chromium-chromedriver

# Set up ChromeDriver
ENV PATH /usr/lib/chromium-browser/:/usr/local/bin/:$PATH

CMD ["python", "app.py"]
