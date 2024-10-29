# Walker_sensorfusion

#############PLAN################

1. Collect Data from Different Sensors

    1.1 Find the Translation/Rotation Matrix between Positions
    1.2 Perform Preliminary Data Logging

2. Develop Measurement Model and Process Model

    2.1 Identify Drift and Uncertainty
    2.2 Build Initial Models: Measurement Model, Process Model
    2.3 Calibrate Using HTC Data

3. Fuse Sensor Data

    3.1 Select and Implement a Fusion Algorithm: eg. kalman, extended kalman or complementary filter
    3.2 Weight Data Based on Uncertainty
    3.3 Implement Real-Time Fusion Pipeline

4. Validation and Testing

    4.1 Compare Fusion Output to Ground Truth (HTC)
    4.2 Error Analysis
    4.3 Tune and Refine
