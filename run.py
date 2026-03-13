from simulator.device import Device

# 流程 1：正常启动和停止
def flow_start_stop():
    device = Device("Robot-01")
    print("FLow 1:")
    print(device.get_status())
    device.start()
    print(device.get_status())
    device.stop()
    print(device.get_status())

# 流程 2：启动 -> 暂停 -> 恢复 -> 停止
def flow_pause_resum():
    device = Device("Robot-02")
    print("\nFlow 2:")
    print(device.get_status())
    device.start()
    print(device.get_status())
    device.pause()
    print(device.get_status())
    device.resume()
    print(device.get_status())
    device.stop()
    print(device.get_status())

# 流程 3：启动 -> 故障 -> 复位
def flow_fail_reset():
    device = Device("Robot-03")
    print("\nFlow 3:")
    print(device.get_status())
    device.start()
    print(device.get_status())
    device.fail()
    print(device.get_status())
    device.reset()
    print(device.get_status())

# 流程 4：错误流程
def invalid_flow():
    device = Device("Robot-04")
    print("\nInvalid flow: pause from IDLE")
    print(device.get_status())

    try:
        device.pause()
    except RuntimeError as e:
        print("Caught error:", e)


def main():
    flow_start_stop()
    flow_pause_resum()
    flow_fail_reset()
    invalid_flow()

if __name__ == "__main__":
    main()