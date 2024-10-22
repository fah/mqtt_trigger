# MQTT Energy Control

MQTT Energy Control is a tiny Python library designed for, for example, energy-saving projects. It allows you to control energy-intensive tasks based on MQTT messages, making it ideal for solar energy systems or other renewable energy applications.

For example: Check the state of the battery or/and the generated solar energy and the do something energy consuming.

## Features

Triggers a function or stops a loop depending on a change on the mqtt server.

1. Loop control: Run a loop while certain energy conditions are met, and pause when energy is insufficient.
2. Trigger functionality: Execute specific functions when energy conditions are met.

## Installation
```sh
    virtualenv venv
    source venv/bin/activate
    pip install paho.mqtt

    pip install mqtt-energy-control
```

No specific python version as ar as "paho.mqtt.client" and "time" libs are available. Testet with Python 3.13 .

## Usage

### Loop Control

```python
from mqtt_energy_control import MQTTEnergyControl

def energy_available(value):
    return float(value) > 1000  # Run when energy is above 1000W

def energy_intensive_task():
    print("Performing energy-intensive task")

controller = MQTTEnergyControl("broker.hivemq.com")
controller.loop_while_condition_met(energy_available, energy_intensive_task)
```


## Condition Examples

### Numeric

```python
# Run when energy is between 1000W and 2000W
def energy_in_range(value):
    return 1000 < float(value) < 2000
```

### Boolean

```python
# Run when system is in "ready" state
def system_ready(value):
    return value.lower() == "ready"
```

### Textual

```python
# Run when status is "optimal"
def optimal_conditions(value):
    return value.strip().lower() == "optimal"
````

This library is designed to help manage energy-intensive tasks in renewable energy systems, ensuring that high-power operations are only performed when sufficient energy is available.

