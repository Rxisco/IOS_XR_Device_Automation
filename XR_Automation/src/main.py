import pandas as pd
from netmiko import ConnectHandler
from datetime import datetime
# Load device information from Excel
df = pd.read_excel('data/data.xlsx')

for index, row in df.iterrows():
    device = {
        'device_type': 'cisco_xr',  # Change as per your device type
        'host': row['hostname'],
        'username': row['username'],
        'password': row['password'],
         'port' :22,
         'timeout': 15,
         # Optional, if you have enable secret
    }

    try:
        # Connect to the device
        with ConnectHandler(**device) as net_connect:
            # Enter enable mode if secret is provided
           
            net_connect.enable()
            
            print(f'{row["hostname"]} connected successfully')
            result=''
            # Split the commands and execute them
            commands = row['commands'].split(',')
            for command in commands:
                output = net_connect.send_command(command)
                print(f"Output from {row['hostname']} for command '{command}':")
                print(output)
                print('-' * 80)
                result+=command+'\n'+output+'\n'+"-----------------"*10 +'\n'
            with open( 'Output/'+row['hostname']+"_"+str(datetime.now())+'.csv','a') as f:
                f.write(result)
            net_connect.disconnect()
        print(f'{row["hostname"]} disconnected successfully')

    except Exception as e:
        print(f"Failed to connect to {row['hostname']}: {e}")
        
                
    print("Configuration completed.")
    
