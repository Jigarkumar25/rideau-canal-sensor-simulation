import time
import json
import random
import os
from datetime import datetime, timezone
from azure.iot.device import IoTHubDeviceClient, Message
from dotenv import load_dotenv

load_dotenv()

DOWS_CONN = os.getenv("DOWS_CONN")
FIFTH_CONN = os.getenv("FIFTH_CONN")
NAC_CONN = os.getenv("NAC_CONN")
SEND_INTERVAL = int(os.getenv("SEND_INTERVAL", "10"))

clients = {
    "Dows Lake": IoTHubDeviceClient.create_from_connection_string(DOWS_CONN),
    "Fifth Avenue": IoTHubDeviceClient.create_from_connection_string(FIFTH_CONN),
    "NAC": IoTHubDeviceClient.create_from_connection_string(NAC_CONN),
}

def generate_data(location: str) -> dict:
    return {
        "location": location,
        "iceThicknessCm": round(random.uniform(20, 40), 2),
        "surfaceTempC": round(random.uniform(-10, 2), 2),
        "snowAccumulationCm": round(random.uniform(0, 10), 2),
        "externalTempC": round(random.uniform(-15, 5), 2),
        "eventTime": datetime.now(timezone.utc).isoformat(),
    }

print("Sending data to IoT Hub... Press CTRL+C to stop.")

while True:
    for location, client in clients.items():
        payload = generate_data(location)
        msg = Message(json.dumps(payload))
        client.send_message(msg)
        print(f"Sent from {location}: {payload}")
    time.sleep(SEND_INTERVAL)
