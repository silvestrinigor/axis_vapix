from requests import Response
import json

def is_response_with_error(response: Response) -> bool:
    json.loads(response.text)
    if 'error' in response:
        return True
    else:
        return False
