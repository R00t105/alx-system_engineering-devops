#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    # Set the User-Agent to avoid 429 errors
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Construct the URL for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        # Make the request with no redirects allowed
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and extract the subscriber count
            return response.json().get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0

# Example usage:
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
