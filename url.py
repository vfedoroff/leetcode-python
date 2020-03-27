from httplib import HTTPSConnection
import json

if __name__ == "__main__":
    connection = HTTPSConnection("www.httpbin.org")
    connection.connect()
    headers = {'Content-type': 'application/json'}
    foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
    payload = json.dumps(foo)
    connection.request('POST', "/post", body=payload, headers=headers)
    response = connection.getresponse()
    print(response.read().decode())