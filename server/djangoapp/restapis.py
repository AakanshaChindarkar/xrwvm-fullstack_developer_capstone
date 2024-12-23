# Uncomment the imports below before you add the function code
# import requests
import os
from dotenv import load_dotenv
import requests

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

   # Log the full URL to verify it's constructed correctly
    print(f"Request URL: {request_url}")

    try:
        # Send the GET request and store the response
        response = requests.get(request_url, timeout=10)  # Timeout after 10 seconds

        # Check the HTTP response code
        if response.status_code == 200:
            return response.json()  # Return JSON if successful
        else:
            # If response is not successful, print the status code and return None
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.Timeout:
        # Handle timeout explicitly
        print("Timeout error: The request timed out.")
        return None
    except requests.exceptions.RequestException as e:
        # Handle any other network-related error
        print(f"Network exception: {e}")
        return None
    except Exception as e:
        # Catch all for any other unexpected errors
        print(f"Unexpected error: {e}")
        return None

def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

#Update the `get_dealerships` render list of dealerships all by default, particular state if state is passed
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")