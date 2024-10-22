from mqtt_trigger import MQTTTrigger
import json

def batteryOver90(value):
    f = float(json.loads(value)["value"])
    print(f)
    return f > 90  # Trigger when SOC exceeds 90%

def loop_high_power_device():
    print("Running high-power device")

controller = MQTTTrigger("192.168.1.111", topic="N/1234/battery/277/Soc")
controller.loop_while_condition_met(batteryOver90, loop_high_power_device, check_interval=2, wait_for_new_arrival=True)
