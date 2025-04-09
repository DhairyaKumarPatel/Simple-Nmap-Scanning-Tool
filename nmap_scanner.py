#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome to simple Nmap Scanning tool !")
print("--------------------------------------")

ip_addr = input("Please enter the IP address to scan : ")
print("The IP entered is :",ip_addr)

print("Type of IP address is :",type(ip_addr))

resp = input("""\n Please Enter the Type of Scan you want to Perform :
	1. SYN Scan
	2. UDP Scan
	3. Comprehensive Scan\n""")
print("You have selected :",resp)

resp_dict = {'1':['-sV -sS -vv','tcp'],'2': ['-sV -sU -vv' ,'udp' ],'3' : ['-A -sS -vv -p-', 'tcp' ]}

if resp not in resp_dict.keys():
	print("Please Enter a Valid Option !! ")
else:
	print("Nmap Version:", scanner.nmap_version())
	scanner.scan(ip_addr, "1-1024",resp_dict[resp][0])
	
	if scanner [ip_addr].state()=='up':
		print("\n Host is up. Scan Results:") 
	
	for proto in scanner[ip_addr].all_protocols():
		print("\nProtocol: {}".format(proto))
		print("Open Ports: {}".format(','.join(map(str,scanner[ip_addr] [proto].keys()))))
	
	for port, info in scanner [ip_addr] [proto].items():
		print("\nPort: {}nService: {}nState: {}".format(port, info['name'], info['state']))
