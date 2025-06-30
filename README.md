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

## Code Architecture
| File | Purpose | Key Features |
|------|---------|--------------|
| `sensor.py` | **Main Control Module** | <ul><li>GPIO4 (Pin7) moisture sensing</li><li>4x daily scheduled email reports</li><li>Real-time status callbacks</li><li>SMTP error handling</li></ul> |
| `test.py` | **Email Verification Module** | <ul><li>SMTP connection testing</li><li>App password validation</li><li>Email template simulation</li></ul> |

## Sensor.py Functional Breakdown
```python
# Key Components:
1. GPIO Configuration:
   - BCM GPIO4 (Physical Pin7)
   - Pull-up resistor enabled
   - 200ms bounce time filtering

2. Email Engine:
   - QQ SMTP (smtp.qq.com:587)
   - STARTTLS encryption
   - Timestamped alerts

3. Scheduling:
   - 07:00, 10:00, 14:04, 16:00 daily
   - Async event loop
## Sensor.py Functional Breakdown
```python
# Key Components:
1. GPIO Configuration:
   - BCM GPIO4 (Physical Pin7)
   - Pull-up resistor enabled
   - 200ms bounce time filtering

2. Email Engine:
   - QQ SMTP (smtp.qq.com:587)
   - STARTTLS encryption
   - Timestamped alerts

3. Scheduling:
   - 07:00, 10:00, 14:04, 16:00 daily
   - Async event loop

## Quick Start
```bash
# 1. Install dependencies
pip install gpiozero schedule smtplib

# 2. Run main program (monitoring + emails)
python3 sensor.py

# 3. Test email functionality separately
python3 test.py
