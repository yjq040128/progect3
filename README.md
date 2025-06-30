# progect3
Raspberry Pi soil moisture monitoring system
# Plant Moisture Monitor with Email Notification

![Hardware Setup](Physical Setup.jpg)

## Project Overview
- **Type**: Agile IoT Sensor System  
- **Platform**: Raspberry Pi  
- **Core Features**:
  - Real-time soil moisture monitoring via GPIO  
  - Automated email alerts via SMTP  
  - Development managed via Scrum + Sprint  

## Key Components
| Component | Description |
|-----------|-------------|
| Digital Soil Moisture Sensor | FC-28 with adjustable threshold |
| Raspberry Pi GPIO | Physical Pin 7 (BCM GPIO4) |
| QQ Mail SMTP | Encrypted email delivery |

## Code Structure
| File | Purpose |  
|------|---------|
| `sensor.py` | **Main program**:<br>- Moisture data collection<br>- Scheduled email triggering<br>- GPIO management |  
| `test.py` | **Email verification**:<br>- SMTP connection test<br>- Alert message simulation |  

## Quick Start
```bash
# 1. Install dependencies
pip install gpiozero schedule smtplib

# 2. Run main program (monitoring + emails)
python3 sensor.py

# 3. Test email functionality separately
python3 test.py
