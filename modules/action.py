def addIPAddr(CLIENTINFO):
    # - Write setting in /etc/dchp/dhcpd.conf   
    DHCPCONF.add()
    # - Set data and insert data in MongoDB
    DATABASE.setDocData(CLIENTINFO)
    INSERT_RESULT = DATABASE.insertDoc()
    ID = INSERT_RESULT.inserted_id
    # -- Check the data has been inserted properly
    SEARCH_COUNT = DATABASE.searchDoc('_id', ID)
    if SEARCH_COUNT == 1:
        print('Insert data successfully!')
    else:
        print('Insert data with problem. Exit.')
        sys.exit()

        
