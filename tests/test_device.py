import pytest
from simulator.device import Device, DeviceState

@pytest.fixture
def device():
    return Device("Robot-Test")

# initail state
def test_initial_state(device):
    assert device.get_status() == DeviceState.IDLE

# idle --> start
def test_start_from_idle(device): 
    device.start()
    assert device.get_status() == DeviceState.RUNNING

# running --> pasue
def test_pause_from_running(device):   
    device.start()
    device.pause()
    assert device.get_status() == DeviceState.PAUSED

# pause --> resume
def test_resume_from_pause(device):    
    device.start()
    device.pause()
    device.resume()
    assert device.get_status() == DeviceState.RUNNING

# running --> stop
def test_stop_from_running(device):
    device.start()
    device.stop()
    assert device.get_status() == DeviceState.IDLE

# running --> fail
def test_fail_from_running(device):
    device.start()
    device.fail()
    assert device.get_status() == DeviceState.ERROR

# idle --> fail
def test_fail_from_idle(device):
    device.fail()
    assert device.get_status() == DeviceState.ERROR

# pause --> fail
def test_fail_from_pause(device):
    device.start()
    device.pause()
    device.fail()
    assert device.get_status() == DeviceState.ERROR

# error --> reset
def test_reset_from_error(device):
    device.start()
    device.fail()
    device.reset()
    assert device.get_status() == DeviceState.IDLE

# Cycle: pasue --> resume
def test_pause_resume_cycle(device):
    device.start()
    device.pause()
    device.resume()
    device.pause()
    device.resume()
    assert device.get_status() == DeviceState.RUNNING

# reset --> restart
def test_restart_after_reset(device):
    device.start()
    device.fail()
    device.reset()
    device.start()
    assert device.get_status() == DeviceState.RUNNING

# idle --> invalid 
@pytest.mark.parametrize("action", ["pause", "resume", "stop", "reset"])
def test_invalid_actions_from_idle(device, action):
    with pytest.raises(RuntimeError):
        getattr(device,action)()

# pause --> invalid 
@pytest.mark.parametrize("action", ["start","stop","pause","reset"])
def test_invalid_actions_from_paused(device, action):
    device.start()
    device.pause()
    with pytest.raises(RuntimeError):
        getattr(device,action)()

# error --> invalid
@pytest.mark.parametrize("action", ["start","stop","pause","resume"])
def test_invalid_actions_from_error(device, action):
    device.fail()
    with pytest.raises(RuntimeError):
        getattr(device,action)()

# error message: idle --> pause
def test_pause_from_idle_message(device):
    with pytest.raises(RuntimeError, match="pause"):
        device.pause()

# error meassahe: idle --> resume
def test_resume_from_idle_message(device):
    with pytest.raises(RuntimeError, match="Device is not paused"):
        device.resume()