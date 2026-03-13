import socket
import threading
import os
from tqdm import tqdm
import pyfiglet
from termcolor import colored

print(colored(pyfiglet.figlet_format('TCP OPEN PORTS CHECKER VERSION 1\n\nSCRIPT MADE BY KRAINIUM\n\nDONT USE VPN TO RUN SCRIPT', font='term'), 'green'))


target_ip = input(colored(pyfiglet.figlet_format("Enter the target IP address: ", font='term'), 'blue'))
print(" ")
start_port = 1
end_port = 65536


if not os.path.exists('opened-ports'):
    os.mkdir('opened-ports')


def check_port(port):
    try:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.settimeout(1)
        
        s.connect((target_ip, port))
        
        with open('opened-ports/open.txt', 'a') as f:
            if port == start_port:
                f.write(f"Target-IP: {target_ip}\n\n")
            f.write(f"Port {port} is opened!\n")
        print(colored(pyfiglet.figlet_format(f"\nPort {port} is open", font='term'), 'red'))
        
        s.close()
    except:
        
        pass



def port_scan():
    
    threads = []
    
    for port in tqdm(range(start_port, end_port+1), desc="Scanning", unit="ports"):
        
        t = threading.Thread(target=check_port, args=(port,))
        
        threads.append(t)
        
        t.start()

    
    for t in threads:
        t.join()

    
    print(colored(pyfiglet.figlet_format("Port scan complete", font='term'), 'blue'))


port_scan()
