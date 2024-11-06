FROM gcc:11
# Install necessary tools
RUN apt-get update && apt-get install -y cmake

# Copy and compile code
COPY . /workspace
WORKDIR /workspace
# Install any additional tools if needed, e.g., `make` or `cmake`
RUN apt-get update && apt-get install -y cmake make