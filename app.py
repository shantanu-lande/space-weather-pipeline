import requests
import json

# The quotation marks here are critical!
API_KEY = "TpDgPRmbfBhNwbDkLwHWdBKR8Wmw7bwGQr7pG7CL"

def fetch_cme_data():
    """Fetches Coronal Mass Ejection (CME) data."""
    url = f"https://api.nasa.gov/DONKI/CME?api_key={API_KEY}"
    print(f"\n--- Fetching CME Data ---")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            print(f"Found {len(data)} CME events.")
            print(f"Latest CME: {data[0].get('startTime')}")
        else:
            print("No CME events found.")
    else:
        print(f"Error fetching CME data: HTTP {response.status_code}")

def fetch_gst_data():
    """Fetches Geomagnetic Storm (GST) data."""
    url = f"https://api.nasa.gov/DONKI/GST?api_key={API_KEY}"
    print(f"\n--- Fetching GST Data ---")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            print(f"Found {len(data)} GST events.")
            print(f"Latest GST: {data[0].get('startTime')}")
        else:
            print("No GST events found.")
    else:
        print(f"Error fetching GST data: HTTP {response.status_code}")

def lambda_handler(event, context):
    print("Initializing Space Weather Pipeline...")
    fetch_cme_data()
    fetch_gst_data()
    return {
        'statusCode': 200,
        'body': 'Space weather data fetched successfully!'
    }
