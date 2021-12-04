import socket as s
import speedtest
import sys
import json
from urllib.request import urlopen
from scapy.all import ARP, Ether, srp

running = True

def main():
    running = True
    print("Shortcut: python3 ip.py 1")
    print("")

    while running == True:
        print("1. Find IP of website")
        print("2. Find your current IP")
        print("3. Find devices connected to your internet")
        print("4. Upload/Download speed test")
        print("5. Overall internet information")
        print("")
        print("Press X to exit")
        print("")
        opt = input("Enter option: ")

        if opt == "1":
            print(websiteIP())
        
        elif opt == "2":
            print(currentIP())

        elif opt == "3":
            print(devices())
        
        elif opt == "4":
            print(speedTest())
        
        elif opt == "5":
            print(internetInfo())

        elif opt.lower() == "x":
            print("Exiting...")
            running = False
            return ""

        else:
            print("")
            print("Don't quite know what you did there...")
            print("Try again ..?")
            print("")

def internetInfo():
    target_ip = input("Enter target ip e.g. 192.168.1.1/24: ")
    st = speedtest.Speedtest()
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    data = json.load(response)

    host = s.gethostname() 
    ip = data['ip']
    post = data['postal']
    city = data['city']
    region = data['region']
    country = data['country']
    org = data['org']

    print(" ")
    print("INTERNET INFORMATION...")
    print("Host:",host)
    print("Local:",ip)
    print("Postal:",post)
    print("City:",city)
    print("Region:",region)
    print("Country:",country)
    print("ISP:",org)
    print(" ")
    print("RUNNING SPEED TEST...")
    print("Download speed: ", st.download())
    print("Upload speed: ", st.upload()) 
    print(" ")

    
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    
    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []
    
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    count = 0
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))
        count += 1 
    print("Devices connected: ", count)
    print(" ")

def speedTest():
    st = speedtest.Speedtest()
    opt = int(input('''What speed do you want to test:  
    
    1. Download Speed  
    2. Upload Speed  
    3. Both 
    
    Input: '''))

    if opt == 1:  
        print("Download speed: ", st.download())  
    
    elif opt == 2: 
        print("Upload speed: ", st.upload()) 
    
    elif opt == 3:  
        print("Download speed: ", st.download())
        print("Upload speed: ", st.upload()) 
    
    else:
        print("An error occured. Try again?") 
        print(speedTest())


def devices():
    target_ip = input("Enter target ip e.g. 192.168.1.1/24: ")
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    
    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []
    
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    count = 0
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))
        count += 1 
    print("Devices connected: ", count)

def websiteIP():
    print("\x1B[3mHttps: is not required\x1B[23m")
    try:
        website = input("Enter a website URL: ")
        final = "IP of website: "+s.gethostbyname(website)
        print(final)
        return ""
    except:
        print("Something went wrong")



def currentIP():
    local = s.gethostbyname(s.getfqdn())
    print("Current IPv4 address: "+local)
    print("")
    opt = input("Want more information? ")
    options = ["yes","y"]

    if opt.lower() in options:
        print("")
        url = "http://ipinfo.io/json"
        response = urlopen(url)
        data = json.load(response)

        host = s.gethostname() 
        ip = data['ip']
        post = data['postal']
        city = data['city']
        region = data['region']
        country = data['country']
        org = data['org']

        print("Host:",host)
        print("Local:",ip)
        print("Postal:",post)
        print("City:",city)
        print("Region:",region)
        print("Country:",country)
        print("ISP:",org)
    
    else:
        None
    
    return ""

try:
    inp = sys.argv[1]
except:
    print(main())

try:
    if inp == "1":
        print(websiteIP())
        running = False
        quit()
    elif inp == "2":
        print(currentIP())
        running = False
        quit()
    elif inp == "3":
        print(devices())
        running = False
        quit()
    elif inp == "4":
        print(speedTest())
        running = False
        quit()
    elif inp == "5":
        print(internetInfo())
        running = False
        quit()

except:
    None
