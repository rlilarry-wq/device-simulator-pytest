# Device Simulator with Automated Tests

A small Python project that simulates a device state machine and verifies its behavior with automated tests using pytest.

## Features

- Device state simulation
- State transitions:
  - IDLE -> RUNNING
  - RUNNING -> PAUSED
  - PAUSED -> RUNNING
  - RUNNING -> ERROR
  - ERROR -> IDLE
- Invalid action protection with exceptions
- Automated tests with pytest

## Project Structure

```text
device_simulator/
├── simulator/
│   ├── __init__.py
│   └── device.py
├── tests/
│   ├── __init__.py
│   └── test_device.py
├── run.py
├── README.md
├── requirements.txt
├── .gitignore
└── pytest.ini
