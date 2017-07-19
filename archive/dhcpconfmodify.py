import sys

def edit(METHOD, DHCPCONF, HOSTNAME, IPADDR, MACADDR):
    with open(DHCPCONF, 'r') as in_file:
        buf = in_file.readlines()

    with open(DHCPCONF, 'w') as out_file:
        for line in buf:
            if METHOD == 'remove':
                if not any(DUPINFO in line for DUPINFO in [HOSTNAME, IPADDR, MACADDR]):
                    out_file.write(line)
            elif METHOD == 'add':
                if  any(DUPINFO in line for DUPINFO in [HOSTNAME, IPADDR, MACADDR]):
                    print('The Infomation you provided has contained in DHCP configurtion file')
                    print('Please check below infomation from dhcp.conf')
                    print('-----------')
                    print(line)
                    print('-----------')
                    continue 
                if line == '# dhcpmgr_ip_list_begin\n':
                    line = line + 'host ' + HOSTNAME + ' ( fixed-address ' + IPADDR + '; hard ethernet ' + MACADDR + '; )\n'
                out_file.write(line)


