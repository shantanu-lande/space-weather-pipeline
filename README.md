

# 🌌 NASA Space Weather Automated Alert Pipeline (DONKI)

> A production-grade, serverless cloud pipeline designed to automatically monitor, fetch, and process real-time Coronal Mass Ejections (CMEs) and Geomagnetic Storms (GSTs) from NASA’s DONKI API. Built for the **NASA Space Apps Challenge**.

---

## 🚀 Architecture & Tech Stack

This project utilizes a modern cloud-native, serverless container architecture hosted on **AWS**:

* **Data Source**: [NASA DONKI API](https://api.nasa.gov/) (Space Weather Database Of Notifications, Knowledge, Information)
* **Core Logic**: Python (`requests`, `json`)
* **Containerization**: Docker (packaged with official AWS Lambda Python Runtime Interface)
* **Cloud Infrastructure (AWS)**:
* **Amazon ECR (Elastic Container Registry)**: Secure storage for versioned container images.
* **AWS Lambda**: Serverless execution environment handling data fetching and pipeline triggers.
* **Amazon EventBridge**: Automated cron scheduler firing pipeline executions on a `rate(1 day)` cadence.


* **Command Center Dashboard**: Responsive HTML5/Tailwind CSS dark-mode telemetry interface with live execution logs.

---

## 📊 System Command Center Dashboard

Included in this repository is the **NASA DONKI Pipeline Dashboard** (`index.html`), providing real-time telemetry, simulated AWS Lambda execution traces, active status monitoring for AWS Lambda and EventBridge, and live data feeds for CMEs and GSTs.

---

## 🛠️ Project Structure

```text
space-weather/
├── app.py              # Main Python script for NASA DONKI API ingestion & Lambda handler
├── Dockerfile          # Container configuration using AWS Lambda base image
├── requirements.txt    # Python dependencies (requests==2.31.0)
└── index.html          # Futuristic web telemetry & monitoring dashboard

```

---

## ⚙️ Quick Start & Deployment Guide

### 1. Local Testing (Docker & Lambda RIE)

To test the containerized Lambda function locally before deploying to AWS:

```bash
# Build the container image
docker build -t space-weather-app .

# Run the container locally on port 9000
docker run -p 9000:8080 space-weather-app

# In a separate terminal tab, trigger the function invocation
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"test"}'

```

### 2. AWS Cloud Deployment (ECR & Lambda)

Follow these standard AWS CLI commands to push your container to the cloud:

```bash
# Authenticate Docker with Amazon ECR
aws ecr get-login-password --region ap-south-2 | docker login --username AWS --password-stdin <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.ap-south-2.amazonaws.com

# Build and tag your repository image
docker build -t space-weather-repo .
docker tag space-weather-repo:latest <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.ap-south-2.amazonaws.com/space-weather-repo:latest

# Push the image to ECR
docker push <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.ap-south-2.amazonaws.com/space-weather-repo:latest

```

### 3. Automated Scheduling (EventBridge)

* Navigate to the **AWS Lambda Console** and create a function from your container image (`space-weather-repo`).
* Add an **Amazon EventBridge** trigger.
* Configure a new schedule rule (e.g., `rate(1 day)`) to automate daily solar activity polling.

---

## 💡 Features

* **Automated Solar Event Tracking**: Pulls latest CME start times, instruments, and planetary magnetic storm indices ($Kp$ indices).
* **Fault-Tolerant Error Handling**: Gracefully handles API rate limits (HTTP 503/429) with built-in status checks and telemetry fallbacks.
* **Zero-Maintenance Serverless Scaling**: Runs entirely on AWS Lambda, scaling to zero when idle to eliminate infrastructure costs.

---

## 🏆 Hackathon Submission Details

* **Event**: NASA Space Apps Challenge
* **Focus Area**: Space Weather Science & Automation

---
