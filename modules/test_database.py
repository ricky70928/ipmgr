from setting import *
from database import *

CLIENTINFO = ['MyHostname', '10.0.0.1', 'aa:bb:cc:dd:ee']

SETTING = setting()
print(SETTING.getClientInfo())
SETTING.setClientInfo(CLIENTINFO)
print(SETTING.getClientInfo())

# Test Database connection and insert document
OPTION = 'hostname'
VALUE = 'MyHostname'
NEWVALUE = 'MyHostname_Modify'
DATABASE = database(SETTING)

print('=== Show Command ===')
print(DATABASE.getDocData())
DATABASE.setDocData(CLIENTINFO)

print('===  Test DB connection and insert Document ===')
DATABASE.connectDB()
print('Data Info: \n {}'.format(DATABASE.getDocData()))

INSERT_RESULT = DATABASE.insertDoc()
print('Insert data. Return code: {}'.format(INSERT_RESULT))

print('===  Test DB search function before remove ===')
SEARCH_COUNT = DATABASE.searchDoc(OPTION, VALUE)
print('Search {} data(s)'.format(SEARCH_COUNT))

print('===  Test DB modify function ===')
print('Modify {}. Current Value: {}. New Value: {}'.format(OPTION, VALUE, NEWVALUE))
MODIFY_RESULT = DATABASE.modifyDoc(OPTION, VALUE, NEWVALUE)
print('Modify data. Return code: {}'.format(MODIFY_RESULT))

print('===  Test DB search function with new value===')
SEARCH_COUNT = DATABASE.searchDoc(OPTION, NEWVALUE)
print('Search {} data(s)'.format(SEARCH_COUNT))

print('===  Test DB remove function with new value===')
REMOVE_RESULT = DATABASE.removeDoc(OPTION, NEWVALUE)
print('Remove data. Return code: {}'.format(REMOVE_RESULT))
