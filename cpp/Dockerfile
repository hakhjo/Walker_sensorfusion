FROM gcc:11

# Install necessary tools
RUN apt-get update && apt-get install -y cmake

# Copy and compile code
COPY . /app
WORKDIR /app
RUN g++ -o read_data read_data.cpp
