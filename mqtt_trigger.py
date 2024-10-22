import paho.mqtt.client as mqtt
import time

class MQTTTrigger:

    def __init__(self, broker, mq_user=None, mq_password=None, port=1883, topic="energy/status", loopTimeSec=2, verbose=False):
        self.client = mqtt.Client()
        self.mq_user = mq_user
        self.mq_password = mq_password
        self.broker = broker
        self.port = port
        self.topic = topic
        self.loopTimeSec = loopTimeSec
        self.latest_value = None
        self.client.on_message = self._on_message
        if (mq_user and mq_password):
            self.client.username_pw_set(mq_user,mq_password)
        # self.client.tls_set(certfile=None,keyfile=None,cert_reqs=ssl.CERT_REQUIRED)
        self.client.connect(broker, port)
        self.client.subscribe(topic)
        self.client.loop_start()
        self.arrival = False # New message arrived
        self.verbose = verbose

    def _on_message(self, client, userdata, message):
        self.latest_value = message.payload.decode()
        if (self.verbose):
            print(self.latest_value)
        self.arrival=True

    # Waits for the condition and returns True, if condition_func returns True.
    # If wait_for_new_arrival=True (default) it is only triggered when new value arrives from MQTT server
    # Param timeout is the max time the loop runs, If None (default) the loops runs forever.,
    def wait_for_condition(self, condition_func, timeout=None, wait_for_new_arrival=True):
        start_time = time.time()
        while True:
            if (self.arrival):
                self.arrival=not wait_for_new_arrival
                if condition_func(self.latest_value):
                    return True
            if timeout and (time.time() - start_time) > timeout:
                return False
            time.sleep(self.loopTimeSec)

    # Wait for new value
    def run_when_condition_met(self, condition_func, action_func, timeout=None):
        if self.wait_for_condition(condition_func, timeout):
            action_func()

    # Loop endless: Trigger when new value arrives and then calls condition function
    # if wait_for_new_arrival is False it is just checking for the condition_func und only wait for the first value to arrive. Then loops ongoing.
    def loop_while_condition_met(self, condition_func, loop_func, check_interval=1, wait_for_new_arrival=True):
        while True:
            if self.wait_for_condition(condition_func, check_interval, wait_for_new_arrival):
                loop_func()
            time.sleep(0.1)

    def __del__(self):
        self.client.loop_stop()
        self.client.disconnect()
