#device.py

class Device:
    """
    Base IoT device
    기반 사물인터넷 장치
    """
    
    def __init__(self, name: str) -> None:
        self.name = name
    
    def connect(self) -> None:
        print(f"self.name} connecting...")
        
    def status(self) -> str:
        return "Unknown"

class SensorDevice(Device):
    """
    A device that reads data.
    데이터를 읽을 수 있는 장치.
    """
    def status(self) -> str:
        return "Reading Data..."

class ActuatorDevice(Device):
    """
    A device that performs actions.
    작동할 수 있는 장치.
    """
    def status(self) -> str:
        return "Performing action..."
    
    
    
    
    
    
    
    