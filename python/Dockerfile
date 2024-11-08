FROM python:3.9


# Install prerequisites for adding the Intel RealSense repository
RUN apt-get update && \
    apt-get install -y wget curl gnupg2 software-properties-common apt-transport-https libusb-1.0-0 libgl1 usbutils udev


# Add the Intel RealSense GPG key
RUN mkdir -p /etc/apt/keyrings && \
    curl -sSf https://librealsense.intel.com/Debian/librealsense.pgp | tee /etc/apt/keyrings/librealsense.pgp > /dev/null

# Add the Intel RealSense repository, forcing the distribution to focal
RUN echo "deb [signed-by=/etc/apt/keyrings/librealsense.pgp] https://librealsense.intel.com/Debian/apt-repo focal main" | tee /etc/apt/sources.list.d/librealsense.list

RUN wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb && \
    dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb
## Download Intel RealSense udev rules
RUN wget https://github.com/IntelRealSense/librealsense/raw/master/config/99-realsense-libusb.rules -O /etc/udev/rules.d/99-realsense-libusb.rules
# Manually download and install libssl1.1 for compatibility
# Update and install RealSense packages, including librealsense2 and librealsense2-utils
RUN apt-get update && \
    apt-get install -y librealsense2 librealsense2-utils 

#librealsense2-dkms
# Set the working directory inside the container
WORKDIR /workspace/python

# Copy requirements.txt from the python context
COPY requirements.txt . 

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the source code
COPY . /workspace
