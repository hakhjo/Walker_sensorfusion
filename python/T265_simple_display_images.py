import pyrealsense2 as rs
import cv2
import cv2
import time
import numpy as np

# try:
#     ctx = rs.context()
#     devices = ctx.query_devices()
#     if not devices:
#         print("No RealSense device detected.")
#     else:
#         for device in devices:
#             print("Device:", device.get_info(rs.camera_info.name))
#             print("Serial Number:", device.get_info(rs.camera_info.serial_number))
# except Exception as e:
#     print("Error:", e)
def display_t265():

    pipeline = rs.pipeline()
    pipeline.start()
    print(" ESC key to terminate")
    time.sleep(2)
    print("GO!")
    try:
        while True:
            frames = pipeline.wait_for_frames()
            f1 = frames.get_fisheye_frame(1)
            f2 = frames.get_fisheye_frame(2)

            if not f1:
                continue
            if not f2:
                continue

            image1 = np.asanyarray(f1.get_data())
            image2 = np.asanyarray(f2.get_data())
            im_v = cv2.hconcat([image1, image2])

            cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('RealSense', im_v)
            pose_frame = frames.get_pose_frame()

            if pose_frame:
                pose_data = pose_frame.get_pose_data()
                print("Position: X = {:.2f}, Y = {:.2f}, Z = {:.2f}".format(
                    pose_data.translation.x,
                    pose_data.translation.y,
                    pose_data.translation.z))
                print("Velocity: X = {:.2f}, Y = {:.2f}, Z = {:.2f}".format(
                    pose_data.velocity.x,
                    pose_data.velocity.y,
                    pose_data.velocity.z))
                print("Acceleration: X = {:.2f}, Y = {:.2f}, Z = {:.2f}".format(
                    pose_data.acceleration.x,
                    pose_data.acceleration.y,
                    pose_data.acceleration.z))

            key = cv2.waitKey(1)
            if key == 27: # ESC
                return



    finally:
        pipeline.stop()

try:
    display_t265()
except Exception as e:
    print("ERROR T265  : ",e)

