"""
Copyright (c) 2018 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Healkan Cheung"
__copyright__ = "Copyright (c) 2018 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"

from cli import *
import requests
requests.packages.urllib3.disable_warnings()

url = "https://api.ciscospark.com/v1/messages"
config_diff = '**Config Changed**\n*A minus symbol (-) indicates configuration line exits in running config but not in start
up config*\n*A plus symbol (+) indicates configuration line exists in startup config but not in running config*\n'
config_diff = config_diff + cli("show archive config diff")
config_diff = config_diff.replace('!Contextual Config Diffs:','')
config_diff = config_diff.replace('\n','  \n')


payload = {'roomId': '<Room ID>', 'markdown' : config_dif
f}

headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer <Bot Access Token>",
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, json=payload, headers=headers, verify = False)

