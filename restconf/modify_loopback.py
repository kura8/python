import json
import requests
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

if __name__ == "__main__":
    
    target_auth = HTTPBasicAuth('developer', 'C1sco12345')
    target_headers = {
        'Accept': 'application/yang-data+json',
        'Content-type': 'application/yang-data+json'
    }
    
    target_body_put = {
        "Loopback":[
            { 
                "name": 444, 
                "ip": { 
                    "address": { 
                        "primary": { 
                            "address": "192.168.44.4",
                            "mask": "255.255.255.0"
                        } 
                    }
                }
            }
        ]
    }
    target_body_patch = {
        "Loopback":[
            { 
                "description": "This is a Test Loopback",
            }
        ]
    }
    target_body_put2 = {
        "Loopback":[
            { 
                "name": 444, 
                "ip": { 
                    "address": { 
                        "primary": { 
                            "address": "192.168.44.4",
                            "mask": "255.255.255.0"
                        } 
                    }
                }
            }
        ]
    }




    target_url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback"
    response = requests.get(target_url, auth=target_auth, headers=target_headers, verify=False)
    response = json.loads(response.text)
    print(json.dumps(response, indent=4))
    print('#' * 30 )

    target_url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=444"
    response = requests.put(target_url, data=json.dumps(target_body_put), auth=target_auth, headers=target_headers, verify=False)
    target_url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback"
    response = requests.get(target_url, auth=target_auth, headers=target_headers, verify=False)
    response = json.loads(response.text)
    print(json.dumps(response, indent=4))
    print('#' * 30 )

    target_url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=444"
    response = requests.patch(target_url, data=json.dumps(target_body_patch), auth=target_auth, headers=target_headers, verify=False)
    target_url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback"
    response = requests.get(target_url, auth=target_auth, headers=target_headers, verify=False)
    response = json.loads(response.text)
    print(json.dumps(response, indent=4))
    print('#' * 30 )

    target_url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=444"
    response = requests.put(target_url, data=json.dumps(target_body_put2), auth=target_auth, headers=target_headers, verify=False)
    target_url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback"
    response = requests.get(target_url, auth=target_auth, headers=target_headers, verify=False)
    response = json.loads(response.text)
    print(json.dumps(response, indent=4))
    print('#' * 30 )

    target_url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=444"
    response = requests.delete(target_url, auth=target_auth, headers=target_headers, verify=False)
    target_url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback"
    response = requests.get(target_url, auth=target_auth, headers=target_headers, verify=False)
    response = json.loads(response.text)
    print(json.dumps(response, indent=4))
    print('#' * 30 )

