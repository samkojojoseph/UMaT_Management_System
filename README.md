# UMaT_Management_System
print("===== SMART DEVICE MANAGEMENT SYSTEM =====")


# Base Class
class SmartDevice:
    def __init__(self, name, device_id):
        self.name = name
        self.__device_id = device_id      # Encapsulated
        self.__power_status = "OFF"       # Encapsulated

    # Getter methods
    def get_device_id(self):
        return self.__device_id

    def get_power_status(self):
        return self.__power_status

    # Setter methods
    def turn_on(self):
        self.__power_status = "ON"
        print(f"{self.name} is ON.")

    def turn_off(self):
        self.__power_status = "OFF"
        print(f"{self.name} is OFF.")

    def display_info(self):
        print("\n=== DETAILS OF DEVICE ===")
        print("Device Name :", self.name)
        print("Device ID   :", self.__device_id)
        print("Power Status:", self.__power_status)


# Light Class
class Light(SmartDevice):
    def __init__(self, name, device_id):
        super().__init__(name, device_id)
        self.brightness = 0

    def adjust_brightness(self):
        value = int(input("Enter brightness (0-100): "))
        if 0 <= value <= 100:
            self.brightness = value
            print("Brightness updated.")
        else:
            print("Invalid brightness.")

    def show_light(self):
        self.display_info()
        print("Brightness:", self.brightness)


# Temperature Sensor Class
class TemperatureSensor(SmartDevice):
    def __init__(self, name, device_id):
        super().__init__(name, device_id)
        self.temperature = 25

    def set_temperature(self):
        self.temperature = float(input("Enter new temperature: "))
        print("New Temperature recorded.")

    def show_temperature(self):
        self.display_info()
        print("Temperature:", self.temperature, "°C")


# Security Camera Class
class SecurityCamera(SmartDevice):
    def __init__(self, name, device_id):
        super().__init__(name, device_id)
        self.recording = False

    def start_recording(self):
        self.recording = True
        print("Device has started recording.")

    def stop_recording(self):
        self.recording = False
        print("Recording has ended.")

    def show_camera(self):
        self.display_info()
        print("Recording:", self.recording)


# Creating Devices
light = Light("Smart Light", "JS145")
sensor = TemperatureSensor("Temperature Sensor", "TS145")
camera = SecurityCamera("Security Camera", "SC145")


# Main Menu
while True:
    print("\n===== MAIN MENU =====")
    print("1.Smart Light")
    print("2.Temperature Sensor")
    print("3.Security Camera")
    print("4.Exit")

    choice = input("Select a smart device: ")

    if choice == "1":         # display menu of light
        sensor_on = False     # device should be turned on before adjustment can be done
        while True:
            print("\n=== Smart light Menu ===")
            print("1.Turn ON device")
            print("2.Turn OFF device")
            print("3.Adjust Brightness")
            print("4.Display Information")
            print("5.Back")

            option = input("Choose: ")

            if option == "1":
                light.turn_on()
                sensor_on = True
            elif option == "2":
                light.turn_off()
                sensor_on = False
            elif option == "3":
                if sensor_on:
                    light.adjust_brightness()
                else:
                    print('Please turn device on first')
            elif option == "4":
                light.show_light()
            elif option == "5":
                break
            else:
                print("Invalid choice. Rechoose option")

    elif choice == "2":     #display menu of temperature sensor
        sensor_on = False    # device should be turned on before adjustment can be done
        while True:
            print("\n=== Temperature Sensor Menu ===")
            print("1.Turn ON device")
            print("2.Turn OFF device")
            print("3.Set Temperature")
            print("4.Display Information")
            print("5.Back")

            option = input("Choose: ")

            if option == "1":
                sensor.turn_on()
                sensor_on= True
            elif option == "2":
                sensor.turn_off()
                sensor_on = False
            elif option == "3":
                if sensor_on:
                    sensor.set_temperature()
                else:
                    print('Please turn device on first')
            elif option == "4":
                sensor.show_temperature()
            elif option == "5":
                break
            else:
                print("Invalid choice. Rechoose option")

    elif choice == "3":       # display menu of security camera
        sensor_on = False     # device should be turned on before adjustment can be done
        while True:
            print("\n=== Security Camera Menu ===")
            print("1.Turn ON device")
            print("2.Turn OFF device")
            print("3.Start Recording")
            print("4.Stop Recording")
            print("5.Display Information")
            print("6.Back")

            option = input("Choose: ")

            if option == "1":
                camera.turn_on()
                sensor_on = True
            elif option == "2":
                camera.turn_off()
                sensor_on = False
            elif option == "3":
                if sensor_on:
                    camera.start_recording()
                else:
                    print('Please turn device on first')
            elif option == "4":
                if sensor_on:
                    camera.stop_recording()
                else:
                    print('Please turn device on first')

            elif option == "5":
                camera.show_camera()
            elif option == "6":
                break

    elif choice == "4":
        print("Update successfully done.")
        break

    else:
        print("Please choose a valid option.")
