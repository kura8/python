from netmiko import ConnectHandler 

device = ConnectHandler(host='sandbox-iosxe-latest-1.cisco.com', username='developer', password='C1sco12345', device_type='cisco_ios')
output = device.find_prompt()
print(output)
device.disconnect