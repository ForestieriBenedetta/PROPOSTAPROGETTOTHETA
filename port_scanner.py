import socket

from termcolor import colored



target = input('Inserisci indirizzo IP da scansionare: ')

portrange = input('Inserire il range di porte da verificare(es 5-200): ')



lowport = int(portrange.split('-')[0])

highport = int(portrange.split('-')[1])



print('Scanning host', target, 'from port', lowport,'to port', highport)



for port in range(lowport,highport + 1):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    status = s.connect_ex((target, port))

    if(status == 0):

        print(colored('Port', 'yellow'), colored(port, 'yellow'), colored('- OPEN', 'yellow'))

    else:    

        print('Port',port, '- CLOSED')

    s.close()

