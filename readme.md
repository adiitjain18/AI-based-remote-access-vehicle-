# AI Based Remote Access Vehicle Monitoring System

## Overview
This project implements an AI-based monitoring system for a Hydraulic Reservoir Tunnel (HRT). It utilizes Raspberry Pi for data collection from various sensors and Pi Cam, employs YOLOv8 for object detection, and integrates with AWS for data storage and real-time communication.

### Key Features
- **Debris and Sedimentation Detection:** Pi Cam captures images processed through YOLOv8 for object detection.
- **Structure Integrity:** Ultrasonic sensor detects cracks in the tunnel structure.
- **Water Purity:** Turbidity, TDS, and temperature sensors ensure water quality meets standards.
- **Real-time Data Display:** Results displayed on a hosted webpage using AWS services.
- **Alert System:** Email alerts triggered for critical issues.

## Technology Stack
- **Hardware:**
  - Raspberry Pi
  - Pi Cam, Ultrasonic, Turbidity, Temperature, TDS sensors
  - Servo motor for camera control

- **Software and AI:**
  - YOLOv8 for object detection
  - AWS Cloud (DynamoDB, MQTT) for data storage and communication
  - Python for script development

## Prototype Model and Circuit
![Architecture](https://github.com/user-attachments/assets/2f4e8cce-1e44-41a9-b5e6-db82f0468679)
![Circuit](https://github.com/user-attachments/assets/90fcf1b0-5b63-403a-ae17-5ea21938fe9d)


## Methodology
1. **Data Collection:** Sensors capture environmental data and images.
2. **AI Processing:** YOLOv8 model analyzes images for debris and objects.
3. **AWS Integration:** Data sent to AWS for storage and real-time updates.
4. **User Interface:** Webpage displays real-time monitoring results.

## Project Status
- **Current Progress:** 80% completion; ongoing improvements and testing.
- **Future Enhancements:** Expand sensor capabilities, optimize AI models, and enhance user interface.

## Repository Structure
- **code/**: Contains Python scripts for sensor data collection, AI processing, and AWS integration.
- **images/**: Circuit diagram and other images used in documentation.
- **README.md**: Project overview and setup instructions.

## Getting Started
To replicate or contribute to this project:
1. Clone this repository.
2. Set up Raspberry Pi and connect sensors as per the circuit diagram.
3. Install required Python dependencies (`pip install -r requirements.txt`).
4. Configure AWS credentials and services (DynamoDB, MQTT).
5. Run the main Python script (`python main.py`) to start data collection and monitoring.

## Contributors
- [Your Name](https://github.com/yourusername)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
