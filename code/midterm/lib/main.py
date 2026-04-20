import sys
sys.path.append('/midterm/lib')
from sensor_module import RoomSensor

kitchen = RoomSensor("Kitchen", 30, 70, 100)
bedroom = RoomSensor("Bedroom", 20, 50, 200)
balcony = RoomSensor("Balcony", 10, 30, 300)

sensor_list = [kitchen, bedroom, balcony]

comfortable_count = 0
normal_count = 0
warning_count = 0

for sensor in sensor_list:
    sensor.show_info()
    
    level = sensor.comfort_level()
    status = sensor.light_status()
    
    print(f"Comfort Level: {level}")
    print(f"Light Status: {status}")
    print("-" * 20)

    if level == "Comfortable":
        comfortable_count += 1
    elif level == "Normal":
        normal_count += 1
    elif level == "Warning":
        warning_count += 1

print(f"Comfortable: {comfortable_count}")
print(f"Normal: {normal_count}")
print(f"Warning: {warning_count}")