#!/usr/bin/python3
import sys, getopt
from modules import dhcpconfmodify

def main(argv):
    DHCPCONF = './doc/dhcp.conf-template'
    METHOD = ''
    HOSTNAME = ''
    IPADDR = ''
    MACADDR = ''
    JOINDNS = 'no'
    try:
        opts, args = getopt.getopt(argv, "M:H:i:m:j:")
    except getopt.GetoptError:
        print('dhcpmgr.py -M <add/remove> -H <hostname> -i <IP address> -m <MAC address> -j <yes/no>')
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

    print('Method is {}'.format(METHOD))
    print('Hostname is {}'.format(HOSTNAME))
    print('IP Address is {}'.format(IPADDR))
    print('MAC Address is {}'.format(MACADDR))
    print('Join DNS is {}'.format(JOINDNS))
    dhcpconfmodify.edit(METHOD, DHCPCONF, HOSTNAME, IPADDR, MACADDR)

if __name__ == "__main__":
    main(sys.argv[1:])
 
