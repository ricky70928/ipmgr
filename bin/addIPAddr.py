#!/usr/bin/python3
import sys, getopt

def main(argv):
    DHCPCONF = '../doc/dhcp.conf-template'
    HOSTNAME = ''
    IPADDR = ''
    MACADDR = ''
    try:
        opts, args = getopt.getopt(argv, "h:i:m:")
    except getopt.GetoptError:
        print('addIPAddr.py -i <IP address> -m <MAC address>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            HOSTNAME = arg
        elif opt == '-i':
            IPADDR = arg
        elif opt == '-m':
            MACADDR = arg

    print('Hostname is {}'.format(HOSTNAME))
    print('IP Address is {}'.format(IPADDR))
    print('MAC Address is {}'.format(MACADDR))
    dhcpconf_modify(DHCPCONF, HOSTNAME, IPADDR, MACADDR)

def dhcpconf_modify(DHCPCONF, HOSTNAME, IPADDR, MACADDR):
    with open(DHCPCONF, 'r') as in_file:
        buf = in_file.readlines()
    with open(DHCPCONF, 'w') as out_file:
        for line in buf:
            if  any(DUPINFO in line for DUPINFO in [HOSTNAME, IPADDR, MACADDR]):
                print('The Infomation you provided has contained in DHCP configurtion file')
                print('Please check below infomation from dhcp.conf')
                print('-----------') 
                print(line)
                print('-----------') 
                print('Exit.')
                sys.exit()
            if line == '# dhcpmgr_ip_list_begin\n':
                line = line + 'host ' + HOSTNAME + ' ( fixed-address ' + IPADDR + '; hard ethernet ' + MACADDR + '; )\n'
            out_file.write(line)

if __name__ == "__main__":
    main(sys.argv[1:])
