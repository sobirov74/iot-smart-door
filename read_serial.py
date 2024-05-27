# import serial
# import requests
# from datetime import datetime

# # Replace 'COM3' with your actual Arduino COM port
# arduino_port = '/dev/tty.usbmodem21201'  # For macOS/Linux, use '/dev/ttyUSB0' or similar
# baud_rate = 9600
# api_url = 'http://localhost:8000/door_opened'  # Replace with your actual FastAPI endpoint

# def read_from_arduino(arduino):
#     try:
#         data = arduino.readline()
#         return data.decode('utf-8').strip()
#     except serial.SerialException as e:
#         print(f"Error reading from serial port: {e}")
#         return None

# def send_post_request():
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     payload = {"timestamp": timestamp}
#     try:
#         response = requests.post(api_url, json=payload)
#         if response.status_code == 200:
#             print("Successfully sent POST request")
#         else:
#             print(f"Failed to send POST request: {response.status_code}")
#     except requests.RequestException as e:
#         print(f"Error sending POST request: {e}")

# def main():
#     try:
#         arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
#         while True:
#             data = read_from_arduino(arduino)
#             if data:
#                 print(f"Received from Arduino: {data}")
#                 if data == "Door Opened":
#                     print("Door opened detected, sending POST request...")
#                     send_post_request()
#     except KeyboardInterrupt:
#         print("Script interrupted by user")
#     except serial.SerialException as e:
#         print(f"Error opening serial port: {e}")
#     finally:
#         if 'arduino' in locals() and arduino.is_open:
#             arduino.close()
#             print("Serial port closed")

# if __name__ == "__main__":
#     main()

# # /dev/tty.usbmodem21201
    


import serial
import requests

# Set up the serial connection (adjust COM port as needed)
ser = serial.Serial('/dev/ttyACM0', 9600)  # Adjust this to match your Arduino's port

def send_post_request():
    url = 'http://localhost:8000/door_opened'
    payload = {'doorStatus': 'open'}
    response = requests.post(url, data=payload)
    print('Status Code:', response.status_code)
    print('Response:', response.text)

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print("Received:", line)
            if line == "Door Opened":
                send_post_request()
except KeyboardInterrupt:
    print("Program stopped manually")
    ser.close()
