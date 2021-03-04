import socket as s
import sys
import json
from urllib.request import urlopen

running = True

def main():
    running = True
    print("Shortcut: python3 ip.py 1")
    print("")

    while running == True:
        print("1. Find IP of website")
        print("2. Find your current IP")
        print("")
        print("Press X to exit")
        print("")
        opt = input("Enter option: ")

        if opt == "1":
            print(websiteIP())
        
        elif opt == "2":
            print(currentIP())

        elif opt.lower() == "x":
            print("Exiting...")
            running = False
            return ""

        else:
            print("")
            print("Don't quite know what you did there...")
            print("Try again ..?")
            print("")


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

except:
    None



