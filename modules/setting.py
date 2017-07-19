class setting:
    def __init__(self):
        # DHCP Setting
        self.DHCPCONF = './doc/dhcp.conf-template'
        # Client Setting
        self.CLIENTINFO = ['default', 'default', 'default']     # HOSTNAME, IPADDR, MACADDRi
        self.DATABASEINFO = ['localhost', 27017, 'ipmgr', 'clients', '']

    def getDHCPInfo(self):
        return self.DHCPCONF

    def getClientInfo(self):
        return self.CLIENTINFO

    def setClientInfo(self, CLIENTINFO):
        self.CLIENTINFO = CLIENTINFO

    def getDBInfo(self):
        return self.DATABASEINFO
