import requests
import json
from requests.auth import HTTPBasicAuth
from requests import Request, Session

def main():
    # req = requests.get('http://pokeapi.co/api/v2/pokemon/1/')
    # print("HTTP Status Code: " + str(req.status_code))
    # print(req.headers)
    # json_response = json.loads(req.content)
    # print("Pokemon Name: " + json_response['name'])

    body = {
            "name": "jenkins-Repo-Staging-WebGoat-Example-11",
            "attributes": { 
               "buildUser": "sotudeko",
               "buildJob": "Repo-Staging/WebGoat-Example",
               "buildId": "9",
               "appVersion": "1.0.3",
               "buildUrl": "http://sola.local:8080/job/Repo-Staging/job/WebGoat-Example/9/",
               "iqScanReportUrl": "http://localhost:8070/ui/links/application/webgoat-ci/report/fb5c070ad8e34eefb6021cbaeec8f3fd"
             }
           }

    auth_data = {
        "j_username": "admin",
        "j_password": "admin123"
    }

# , 'Accept-Encoding': 'identity'

    headers = {"Content-Type": "application/json", "accept": "application/json"}
    url = "http://localhost:8081/service/rest/v1/tags"

    newbody = {"name:", "jenkins-Repo-Staging-WebGoat-Example-12"}

# req = Request('POS', url, data=newbody, headers=headers)
    # req = requests.post(url, data=auth_data, json=body, headers=headers)
    req = requests.post(url, json=body, auth=('admin', 'admin123'), headers=headers)

    print("HTTP Status Code: " + str(req.status_code))
    print("HTTP Status Content: " + str(req.content))

    # json_response = json.loads(req.content)
    # print json_response

if __name__ == '__main__':
    main()

