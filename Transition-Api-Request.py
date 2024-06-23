import requests
from requests.auth import HTTPBasicAuth
import json

def get_transition_id(jira_url, issue_key, username, api_token, status_name="In Progress"):
    # Set up the URL for the transitions API
    url = f"{jira_url}/rest/api/2/issue/{issue_key}/transitions"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    # Make the GET request to the transitions API
    response = requests.get(url, headers=headers, auth=HTTPBasicAuth(username, api_token))
    
    if response.status_code == 200:
        transitions = response.json().get('transitions', [])
        
        # Print transitions for debugging
        print(json.dumps(transitions, indent=2))
        
        # Iterate through the transitions to find the one with the desired status name
        for transition in transitions:
            if transition['name'].lower() == status_name.lower():
                return transition['id']
        
        # If the desired status name is not found
        return None
    else:
        # Handle errors
        print(f"Failed to get transitions. Status code: {response.status_code}")
        print(response.json())
        return None

# Example usage
jira_url = 'https://ezechinedum504.atlassian.net'
issue_key = 'TP-1'  # Replace with your issue key
username = 'ezechinedum504@gmail.com'
api_token = ''

transition_id = get_transition_id(jira_url, issue_key, username, api_token, "In Progress")

if transition_id:
    print(f"The transition ID for 'In Progress' is: {transition_id}")
else:
    print("The transition for 'In Progress' was not found.")
