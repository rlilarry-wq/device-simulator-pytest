from enum import Enum

class DeviceState(Enum):
    IDLE = "IDLE"
    PAUSED = "PAUSED"
    RUNNING = "RUNNING"
    ERROR = "ERROR"

class Device:
    def __init__(self, name: str):
        self.name = name
        self.state = DeviceState.IDLE

    def start(self):
        if self.state != DeviceState.IDLE:            #if self.state != DeviceState.IDLE and self.state != DeviceState.PAUSED:
            raise RuntimeError("Device cannot be started from current state")
        self.state = DeviceState.RUNNING

    def stop(self):
        if self.state != DeviceState.RUNNING:
            raise RuntimeError("Device can not be stopped")
        self.state = DeviceState.IDLE

    def reset(self):
        if self.state != DeviceState.ERROR:
            raise RuntimeError("Reset only allowed from ERROR state")
        self.state = DeviceState.IDLE

    def fail(self): 
        self.state = DeviceState.ERROR

    def pause(self): 
        if self.state != DeviceState.RUNNING:
            raise RuntimeError("Device can only pause when RUNNING")
        self.state = DeviceState.PAUSED
    
    def resume(self):
        if self.state != DeviceState.PAUSED:
            raise RuntimeError("Device is not paused")
        self.state = DeviceState.RUNNING

    def get_status(self):
        return self.state
