a = {'HP': 20, 'DELL': 50, 'MACBOOK': 12, 'ASUS' : 30}

def getcomputer(Total):
    print('Total:')
    print(str(a['HP']) + '  HP')
    print(str(a['DELL']) + ' DELL')
    print(str(a['MACBOOK']) + ' MACBOOK') 
    print(str(a['ASUS']) + ' ASUS')  

    itemTotal = sum(Total.values())
    print('Total number of items: ' + str(itemTotal)) 
    return itemTotal

    getcomputer(a)