# To call an API in Python, you typically use the requests library, which simplifies making HTTP requests.
# First, you need to install the requests library if you haven't already done so.
# You can install it using pip:
# pip install requests

# Import the requests library to make HTTP requests
import requests
import json

# Create an empty list to store the comic numbers
comic_numbers = []

# Loop through the XKCD comics with numbers ranging from 2000 to 2992
for i in range(2000, 2993):
    # Define the base URL for the XKCD API
    base_url = f"https://xkcd.com/{i}/info.0.json"

    # Send a GET request to the XKCD API to fetch the comic data
    response = requests.get(base_url)

    # Parse the JSON response
    data = response.json()

    # Check if the safe title of the comic contains the phrase "what to Do"
    if "what to Do" in data["safe_title"]:
        # If found, append the comic number to the list
        comic_numbers.append(data["num"])

# Print the list of comic numbers
print(comic_numbers)

# Alternatively, you can send a GET request to the XKCD API for a specific comic (e.g., comic number 2000)
comic_url = "https://xkcd.com/2000/info.0.json"
response = requests.get(comic_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Check if the safe title of the comic contains the word "computer"
    if "computer" in data["safe_title"]:
        # Print the safe title of the comic
        print(data["safe_title"])
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")
