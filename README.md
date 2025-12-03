# Rideau Canal IoT Sensor Simulation  
CST8916 Final Project – Sensor Simulation Component

## Student Information
- **Name:** Jigarkumar Dilipkumar Patel  
- **Student ID:** 041169204  
- **Course:** CST8916 – Fall 2025  

---

## Overview

This repository contains a **Python-based IoT sensor simulator** used in the Rideau Canal IoT Monitoring System.  
The simulator mimics real-world environmental sensors installed along the Rideau Canal and continuously sends telemetry data to **Azure IoT Hub**.

The simulator generates and transmits:
- Ice thickness
- Temperature
- Snow depth

This data is later processed by Azure Stream Analytics and displayed on the live web dashboard.

---

## Technologies Used

- Python 3
- Azure IoT Device SDK for Python
- JSON
- Random data generation libraries

---

## Prerequisites

Before running the simulator, you must have:

- Python 3 installed
- An active Azure IoT Hub
- At least one registered IoT device in Azure IoT Hub
- IoT device **connection string**
- `pip` package manager

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Jigarkumar25/rideau-canal-sensor-simulation.git
cd rideau-canal-sensor-simulation
```
### 2. Install Required Package

Install the Azure IoT SDK for Python using `pip`:

```bash
pip install azure-iot-device
```
### Configuration

Open the simulator file (for example: sensor_simulator.py) and update the connection string:
```bash
CONNECTION_STRING = "IoT-Device-Connection-String"
```
### Usage

To start sending live sensor data to Azure IoT Hub:
```bash
python sensor_simulator.py
```
While the program is running:
- Data is sent continuously to Azure IoT Hub  
- Messages can be seen in IoT Hub metrics  
- Stream Analytics receives the data as input  

To stop the simulator, press:
```bash
CTRL + C
```
### Code Structure
#### Main Components

sensor_simulator.py<br>
- The main Python file responsible for generating and sending sensor data to Azure IoT Hub.

Key Functions:
- generate_sensor_data() <br>
Generates random values for ice thickness, temperature, and snow depth.

- send_to_iot_hub()<br>
Sends formatted JSON telemetry to Azure IoT Hub using the Azure IoT SDK.

- main()<br>
Controls the execution of the program and runs the continuous sending loop.

#### Sensor Data Format
JSON Schema
```json
{
  "deviceId": "string",
  "location": "string",
  "iceThickness": "number",
  "temperature": "number",
  "snowDepth": "number",
  "timestamp": "string"
}
```

Example Output
```json
{
  "deviceId": "sensor-001",
  "location": "Dows Lake",
  "iceThickness": 29.4,
  "temperature": -5.8,
  "snowDepth": 3.6,
  "timestamp": "2025-01-12T23:15:30Z"
}
```

## Simulated Locations

The simulator sends data for the following Rideau Canal locations:

- **Dows Lake**  
- **Fifth Avenue**  
- **NAC (National Arts Centre)**  

Each location acts as an independent IoT sensor device.

---

## Role in the Overall System

The sensor simulator is the **data source** for the entire Rideau Canal IoT Monitoring System:

**Sensor Simulator → Azure IoT Hub → Stream Analytics → Cosmos DB & Blob Storage → Web Dashboard(Only from Cosmos DB)**

---

## Troubleshooting

### Common Issues and Fixes

---

### 1. Cosmos DB Document ID Error (`{id}` vs `id`)

**Cause:**  
Initially, the Stream Analytics query was sending the document ID as `{id}` instead of a proper `id` field. Cosmos DB requires a valid `id` property for every document, and because of this mismatch, data was failing to insert correctly.

**Fix:**  
The Stream Analytics SQL query was updated to explicitly generate and assign a valid `id` field using location and timestamp:

```sql
CONCAT(location, '_', FORMAT(System.Timestamp, 'yyyyMMddHHmmss')) AS id
```
---

### 2. No Messages Appearing in IoT Hub  
**Cause:** Simulator not sending data correctly.  
**Fix:**
- Ensure the simulator is running  
- Verify the device exists in IoT Hub  
- Check your internet connection  

---

## AI Tools Disclosure

ChatGPT was used for documentation wording and minor debugging guidance.  
All sensor simulator coding, Azure configuration, testing, and execution were completed manually by me.

---

## References

- Microsoft Azure IoT Hub Python SDK Documentation  
  https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-python-get-started  

- Azure IoT Hub Messaging Documentation  
  https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-messaging  

- Python Official Documentation  
  https://docs.python.org/3/  
