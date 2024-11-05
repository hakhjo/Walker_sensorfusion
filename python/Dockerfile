FROM python:3.10

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY . /app
WORKDIR /app
