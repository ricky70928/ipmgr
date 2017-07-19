import sys

from modules.setting import *

class dhcpconf(setting):
    def __init__(self, DHCPInfo):
        self.DHCPCONF = DHCPInfo.getDHCPInfo()
        self.CLIENTINFO = DHCPInfo.getClientInfo()

    def add(self):
        with open(self.DHCPCONF, 'r') as in_file:
            self.buf = in_file.readlines()
        
        with open(self.DHCPCONF, 'w') as out_file:
            for line in self.buf:
                if any(DUPINFO in line for DUPINFO in self.CLIENTINFO):
                    continue
                if line == '# dhcpmgr_ip_list_begin\n':
                    line = line + 'host ' + self.CLIENTINFO[0] + ' ( fixed-address ' + self.CLIENTINFO[1] + '; hard ethernet ' + self.CLIENTINFO[2] + '; )\n'
                out_file.write(line)

    def remove(self):
        with open(self.DHCPCONF, 'r') as in_file:
            self.buf = in_file.readlines()
        
        with open(self.DHCPCONF, 'w') as out_file:
            for line in self.buf:
                if not any(DUPINFO in line for DUPINFO in CLIENTINFO):
                    out_file.write(line)

    def modify(self, ORIGSTR, NEWSTR):
        with open(self.DHCPCONF, 'r') as in_file:
            self.buf = in_file.readlines()

        with open(self.DHCPCONF, 'w') as out_file:
            for line in self.buf:
                line.replace(ORIGSTR, NEWSTR)
                out_file.write(line)
