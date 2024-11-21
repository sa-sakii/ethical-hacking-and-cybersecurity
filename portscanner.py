import socket   # to communicate with other nodes in the network 
import termcolor        # for colorful output 

def scan(target, ports):
        print(f'\nStarting scan for {str(target)}')
        for port in range(1, ports): 
                scan_port(target, port) 

def scan_port(ipaddress, port):
        try: 
                sock = socket.socket()  # initiating the socket object 
                sock.connect((ipaddress, port))
                print(f"[+] Port opened {str(port)}")
                sock.close()
        except:
                pass


targets = input("[*] Enter the targets IP address to scan (split them by ,) : ")
ports = int(input("[*] Enter how many ports you want to scan: "))

if ',' in targets: 
        print(termcolor.colored(("[*] Scanning multiple targets"), 'red'))
        for ip_addr in targets.split(','):
                scan(ip_addr.strip(' '), ports)
else: 
        scan(targets, ports)
