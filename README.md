# Overview
This python script will send the configuration change on a IOS-XE router to a WebEx Teams Room.  
Whenever a configuration change is made in the CLI, an EEM (Embedded Event Manager) script is triggered and a Python script is activated in the onboard guestshell.  The Python script will send the configuration changes to a WebEx Teams room using a WebEx Teams Bot.

![](./ChatBot.png)


# Prerequisites
- IOS-XE device that supports on-board guestshell.  In this project a CSR1000v runnning 16.06.02 is used.
- A WebEx Teams account
- You will need to create a Room and obtain the Room ID.
- A Webex Teams Bot.  Please go to https://developer.webex.com/ for instruction on creating a Bot.  You will need the Bot Token.

# IOS-XE Configuration
The key configuration is the [EEM script](./EEM.cfg)

Whenever a CLI config change is made, a syslog message "%SYS-5-CONFIG_I: Configured from" will be generated.  The EEM script will look for this syslog pattern:

   **_event syslog pattern "%SYS-5-CONFIG_I: Configured from"_**

and activate the Python script in the guestshell:

   **_action 1.0 cli command "guestshell run python /bootflash/ConfigDiff.py"_**

# Python Script
The [python script](./ConfigDiff.py) imports the following Python modules:

   **_from cli import \*_**  This module allows Python to ru IOS-XE commands
   
   **_import requests_**     This allows REST API so the script can send POST request to WebEx Teams
