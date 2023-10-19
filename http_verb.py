import http.client

host = input("Inserire host/IP del sistema target: ")
port = input("Inserire la porta del sistema target (default:80): ")
path = input("Inserire il path: ")
verb = input("Inserire il verbo da testare: ")

if(port == ""):
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request(verb, path)
    response = connection.getresponse()
    print("Il verbo:", verb, "ha risposto:", response.status)
    connection.close()
except ConnectionRefusedError:
    print("Connessione fallita")
