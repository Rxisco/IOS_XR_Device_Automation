
# ISO XR Device Automation with Excel Input
# Overview

This is a two-part automation where a python script is executed locally or from remote session on the XR devices to retrieve configuration data, that can be further processed locally to validate the field commisioning with design.

# Data Sheet
The data sheet is an excel sheet containing device hostname or IP followed by username and password. This same sheet is used to list out commands to be executed in XR devices in separate collum. The last collum is to save the output retrieved.
# 1. Python Script
SSH to the XR devices to execute the commands listed in Data file.

# 2. VBA Script
This data sheet can then be emailed to backend engineer to execute data validation script which is in VBA.

# Design Philosophy
The script with python & VBA code may be intercepted by antivirus and firewalls, to avoid file corruption the code files, "Data" file and code files are kept separate. This will allow seamless flow of data file over emails.

# Features
* Data-Driven Automation: Utilize input data from Excel to control the XR device dynamically.
* Customizable Parameters: Easily modify parameters in the Excel file to adjust the behavior of the XR device.
* User-Friendly: Minimal setup required, making it accessible even for users with limited programming experience.
# Requirements
* MS Excel (VBA) 
* Python 3.x
* Libraries:
    * pandas (for handling Excel files)
    * netmiko(for device interaction)
      
