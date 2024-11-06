FROM python:3.9

# Set the working directory inside the container
WORKDIR /workspace/python

# Copy requirements.txt from the python context
COPY requirements.txt . 

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the source code
COPY . /workspace
