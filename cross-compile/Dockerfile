FROM ubuntu:20.04
# Install cross-compilation tools
RUN apt-get update && apt-get install -y \
    gcc-aarch64-linux-gnu \
    g++-aarch64-linux-gnu \
    cmake \
    make \
    && rm -rf /var/lib/apt/lists/*

# Create output directory for the compiled binary
RUN mkdir -p /output

# Copy the source file (adjust path if needed)
COPY ../cpp/read_data.cpp /workspace//read_data.cpp
WORKDIR /workspace

# Compile the C++ file for the target architecture
RUN aarch64-linux-gnu-g++ -o /output/robot_program read_data.cpp
