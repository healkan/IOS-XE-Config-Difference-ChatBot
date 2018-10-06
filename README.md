# Overview
This python script will send the configuration change on a IOS-XE router to a WebEx Teams Room.  
Whenever a configuration change is made in the CLI, an EEM (Embedded Event Manager) script is triggered and a Python script is activated in the onboard guestshell.  The Python script will send the configuration changes to a WebEx team room.

![](./ChatBot.png)


# Prerequisites
- IOS-XE device that supports on-board guestshell.  In this project a CSR1000v runnning 16.06.02 is used.
- A WebEx Teams account
- A Webex Teams Bot.  Please go to https://developer.webex.com/ for instruction on creating a Bot.

# IOS-XE Configuration
The key configuration is the [EEM script](./EEM.cfg)
Whenever a CLI config change is made, a syslog message "%SYS-5-CONFIG_I: Configured from" will be generated.  The EEM will look for this syslog pattern 

and activate the Python script in the guestshell
 
**action 1.0 cli command "guestshell run python /bootflash/ConfigDiff.py"**
