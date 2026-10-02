# 🚜 AgCane – Automatic Stop and Data Capture Module

An IoT-based automated vehicle system that uses **RFID technology** to detect predefined points, automatically stop the vehicle, and send the detected RFID data to a **Flask web server** for real-time monitoring.

The project demonstrates the integration of **embedded systems, RFID, motor control, Wi-Fi communication, HTTP communication, Python Flask, and web-based data visualization**.

---
## 📌 Project Overview

AgCane is an automated moving vehicle designed to identify predefined checkpoints using RFID tags.

An **RC522 RFID reader** is mounted on the vehicle and connected to a **NodeMCU ESP8266**. When the vehicle reaches an RFID-tagged checkpoint, the RFID reader detects the tag and obtains its unique ID.

The vehicle then:

1. Detects the RFID tag.
2. Automatically stops.
3. Identifies the detected RFID point.
4. Sends the RFID information to a Flask server through Wi-Fi.
5. Records the data with a timestamp.
6. Displays the captured information on a web dashboard.

This provides an automated way of identifying checkpoints and digitally recording the corresponding data.

---

## 🎯 Objectives

- To develop an automated moving vehicle.
- To detect predefined checkpoints using RFID.
- To automatically stop the vehicle when an RFID tag is detected.
- To capture the unique RFID UID.
- To transmit the captured information using Wi-Fi.
- To develop a Flask-based web server for receiving the data.
- To display RFID data and timestamps on a web dashboard.

---

## ⚙️ Key Features

- 🚗 Automated vehicle movement
- 📡 RFID-based checkpoint detection
- 🛑 Automatic stopping
- 🆔 Unique RFID UID detection
- 📶 ESP8266 Wi-Fi communication
- 🌐 Flask web server
- 🕒 Timestamp-based data recording
- 📊 Web dashboard for captured data
- 🔄 Real-time data transmission

---

## 🔧 Hardware Components

| Component | Purpose |
|---|---|
| NodeMCU ESP8266 | Main controller and Wi-Fi communication |
| RC522 RFID Reader | Detects RFID tags |
| RFID Tags | Represent predefined checkpoints |
| L298N Motor Driver | Controls the motors |
| DC Geared Motors | Moves the vehicle |
| Robot Chassis | Vehicle platform |
| 18650 Battery | Power supply |
| Jumper Wires | Circuit connections |
| Switch | Power control |

---

## 💻 Software & Technologies

- **Arduino IDE**
- **C/C++**
- **ESP8266**
- **RFID**
- **SPI Protocol**
- **Wi-Fi**
- **HTTP**
- **Python**
- **Flask**
- **HTML**
- **CSS**
