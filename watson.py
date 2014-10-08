import json
import requests
from requests.auth import HTTPBasicAuth

import config


# Given a question, query Watson for the answer
# Returns the entire json response
def ask(question):
    URL = "https://watson-wdc01.ihost.com/instance/505/deepqa/v1/question"

    payload = {
        "question": {
            "questionText": question
        }
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-SyncTimeout": 30
    }

    r = requests.post(URL, data=json.dumps(payload),
                      headers=headers,
                      auth=(config.auth["user"], config.auth["pass"]))

    if r.status_code == 200:
        return r.json()
    else:
        # TODO: Signal an error here
        return None

if __name__ == "__main__":
    print ask("Where can I find food for my pet?")
