#!/usr/bin/python3
import sys, getopt

from modules.setting import *
from modules.dhcpconf import *
from modules.database import *
from modules.functions import *

def main(argv):
    HELP = 'ipmgr.py -M <add/remove> -H <hostname> -i <IP address> -m <MAC address> -j <yes/no>'
    try:
        opts, args = getopt.getopt(argv, "M:H:i:m:j:")
    except getopt.GetoptError as err:
        print(HELP)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-M':
            METHOD = arg
        elif opt == '-H':
            HOSTNAME = arg
        elif opt == '-i':
            IPADDR = arg
        elif opt == '-m':
            MACADDR = arg
        elif opt == '-j':
            JOINDNS = arg

    CLIENTINFO = [HOSTNAME, IPADDR, MACADDR]
    
    ### Plan to seprate to another class action.set
    # Read Setting from Object
    SETTING = setting()
    DHCPCONF = dhcpconf(SETTING)
    
    # Connect to MongoDB 
    DATABASE = database()
    DATABASE.connectDB()
   
    # Parser 
    SETTING.setClientInfo(CLIENTINFO)
    DATABASE.setDocData(CLIENTINFO)
    
    ### Plan to seprate to another class action.add
    # Action - Add
    # - Write setting in /etc/dchp/dhcpd.conf
    DHCPCONF.add()
    INSERT_RESULT = DATABASE.insertDoc()

    ### Plan to seprate to another class action.modify
    # Action - Modify
    
    ### Plan to seprate to another class action.search
    # Action - Search
    DHCPCONF.search(ORIGSTR, NEWSTR)
    SEARCH_RESULT = DATABASE.searchDoc(OPTION, VALUE)
    ### Plan to seprate to another class action.remove
    # Action - Remove
    # - Write setting in /etc/dchp/dhcpd.conf
    DHCPCONF.remove()
    REMOVE_RESULT = DATABASE.removeDoc()

    

if __name__ == "__main__":
    main(sys.argv[1:])
