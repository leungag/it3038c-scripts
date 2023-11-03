import requests

# Make a GET request to your Node.js API running on localhost:3000
response = requests.get("http://localhost:3000")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response from the API
    data = response.json()

    # Loop through the data and print widget names and their colors
    for widget in data:
        widget_name = widget.get("name", "Unknown Widget")
        widget_color = widget.get("color", "Unknown Color")
        print(f"{widget_name} is {widget_color}.")
else:
    print(f"Failed to retrieve data from the API. Status code: {response.status_code}")
