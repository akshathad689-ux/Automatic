# 🚜 AgCane – Automatic Stop and Data Capture Module

An IoT-based automated vehicle system designed to detect predefined points using **RFID technology**, automatically stop at the detected point, and capture the corresponding data with a timestamp.

The system combines **NodeMCU (ESP8266), RFID (RC522), motor control, and a Flask web server** to create a simple real-time data capture system.

---

## 📸 Working Model

![AgCane Working Model](images/agcane-working-model.jpg)

---

## 🎥 Project Demonstration

The demonstration shows the vehicle moving along the track, detecting an RFID tag, automatically stopping, and sending the captured information to the web dashboard.

**Demo Video:** `videos/agcane-demo.mp4`

---

## 📌 Problem Statement

In automated agricultural and field-based systems, it can be difficult to accurately identify specific locations and record data when a vehicle reaches predefined points.

Manual monitoring can result in:

- Location identification errors
- Delayed data recording
- Manual intervention
- Difficulty in maintaining time-based records

AgCane addresses this by automatically identifying predefined points using RFID and recording the corresponding data digitally.

---

## 💡 Proposed Solution

AgCane is a small automated vehicle equipped with an **RFID reader**.

When the
