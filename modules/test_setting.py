from modules.setting import *
from modules.dhcpconf import *

CLIENTINFO = ['MyHostanem', '10.0.0.1', 'aa:bb:cc:dd:ee']

SETTING = setting()
print(SETTING.getClientInfo())
SETTING.setClientInfo(CLIENTINFO)
print(SETTING.getClientInfo())
DHCPCONF = dhcpConf(SETTING)
DHCPCONF.add()
