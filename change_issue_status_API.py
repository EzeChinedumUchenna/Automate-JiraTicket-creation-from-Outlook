import requests
from requests.auth import HTTPBasicAuth
import json


def change_issue_status(jira_url, issue_key, username, api_token):
    # Set up the URL for the transitions API
    url = f"{jira_url}/rest/api/2/issue/{issue_key}/transitions"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    payload = json.dumps({
        "transition": {
            "id": "11"
        }
    })
    
    # Make the POST request to the transitions API
    response = requests.post(url, headers=headers, data=payload, auth=HTTPBasicAuth(username, api_token))
    
    if response.status_code == 204:
        print(f"Issue {issue_key} successfully transitioned.")
    else:
        print(f"Failed to transition issue {issue_key}. Status code: {response.status_code}")
        print(response.json())

# Example usage
jira_url = 'https://ezechinedum504.atlassian.net'
issue_key = 'TP-2'  # Replace with your issue key
username = 'ezechinedum504@gmail.com'
api_token = ''




change_issue_status(jira_url, issue_key, username, api_token)
