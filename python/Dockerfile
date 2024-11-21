#FOR WINDOWS
# Start with the Python base image for Windows
FROM mcr.microsoft.com/windows/servercore:ltsc2022

# Set the working directory inside the container
WORKDIR C:\workspace\python

# Install Chocolatey for package management
RUN powershell -NoProfile -Command \
    Set-ExecutionPolicy Bypass -Scope Process -Force; \
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; \
    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install prerequisites
RUN choco install -y \
    wget \
    curl \
    cmake \
    python3 \
    visualstudio2019buildtools \
    git \
    openssl

# Add Python and pip to PATH
RUN setx PATH "%PATH%;C:\Python39\Scripts;C:\Python39"

# Add the Intel RealSense repository and install dependencies
# Note: Adjust the paths or versions as required for Windows
RUN powershell -Command \
    Invoke-WebRequest -Uri https://librealsense.intel.com/releases/v2.50.0 -OutFile librealsense.zip; \
    Expand-Archive -Path librealsense.zip -DestinationPath C:\workspace\librealsense; \
    cd C:\workspace\librealsense; \
    mkdir build; \
    cd build; \
    cmake ..; \
    msbuild ALL_BUILD.vcxproj /p:Configuration=Release

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Copy the rest of the source code
COPY . C:\workspace

# Define the default command
CMD ["python", "app.py"]






#FOR LINUX
# # Start with the Python base image
# FROM python:3.9

# # Install prerequisites
# RUN apt-get update && \
#     apt-get install -y wget curl gnupg2 software-properties-common apt-transport-https libusb-1.0-0-dev libgl1 usbutils udev cmake build-essential libssl-dev libudev-dev pkg-config libgtk-3-dev libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev

# # # Install prerequisites for adding the Intel RealSense repository
# # RUN apt-get update && \
# #     apt-get install -y wget curl gnupg2 software-properties-common apt-transport-https libusb-1.0-0 libgl1 usbutils udev


# # Add the Intel RealSense GPG key
# RUN mkdir -p /etc/apt/keyrings && \
#     curl -sSf https://librealsense.intel.com/Debian/librealsense.pgp | tee /etc/apt/keyrings/librealsense.pgp > /dev/null

# # Add the Intel RealSense repository, forcing the distribution to focal
# RUN echo "deb [signed-by=/etc/apt/keyrings/librealsense.pgp] https://librealsense.intel.com/Debian/apt-repo focal main" | tee /etc/apt/sources.list.d/librealsense.list

# # Manually install libssl1.1, which is required for librealsense dependencies
# RUN wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb && \
#     dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb && \
#     rm libssl1.1_1.1.1f-1ubuntu2_amd64.deb

# # Update package list and install specific versions of librealsense2 and required dependencies
# RUN apt-get update && \
#     apt-get install -y librealsense2=2.50.0-0~realsense0.6128 \
#                        librealsense2-utils=2.50.0-0~realsense0.6128 \
#                        librealsense2-gl=2.50.0-0~realsense0.6128 \
#                        librealsense2-net=2.50.0-0~realsense0.6128

# # Add the RealSense udev rules without reloading
# RUN wget https://github.com/IntelRealSense/librealsense/raw/master/config/99-realsense-libusb.rules -O /etc/udev/rules.d/99-realsense-libusb.rules

# # Add the RealSense udev rules without attempting to reload them here
# RUN wget https://github.com/IntelRealSense/librealsense/raw/master/config/99-realsense-libusb.rules -O /etc/udev/rules.d/99-realsense-libusb.rules


# # # Verify that the directory exists
# # RUN ls -l /tmp/librealsense/librealsense-2.50.0

# # # Build and install librealsense from source in /tmp/librealsense/librealsense-2.50.0
# # RUN cd /tmp/librealsense/librealsense-2.50.0 && \
# #     mkdir build && cd build && \
# #     cmake .. && \
# #     make -j$(nproc) && \
# #     make install && \
# #     ldconfig

# # # After build, move any needed files to /workspace for persistent storage
# # RUN mkdir -p /workspace && \
# #     cp -r /tmp/librealsense/librealsense-2.50.0 /workspace/
# #Download and apply udev rules for RealSense devices
# # RUN wget https://github.com/IntelRealSense/librealsense/raw/master/config/99-realsense-libusb.rules -O /etc/udev/rules.d/99-realsense-libusb.rules && \
# #     udevadm control --reload-rules && udevadm trigger

# # Set the working directory inside the container
# WORKDIR /workspace/python

# # Copy requirements.txt and install Python dependencies
# COPY requirements.txt .
# RUN pip3 install -r requirements.txt

# # Copy the rest of the source code
# COPY . /workspace
