import socket # comunicação via tcp / udp outras máquinas
import termcolor # color stuff


def scan (target, ports):
        print('\n' + 'Fazendo scan de ' + str(target))
        for port in range(1, ports):
                scan_port(target, port)

def scan_port(ipaddress, port) :
    try:
        # inicia o objeto socket
        sock = socket.socket()
        # Se connect == porta aberta | se não == fechada
        sock.connect((ipaddress, port)) # coecta a uma porta de um ip
        print("[+] Port open " + str(port))
        sock.close() # Fechar o objeto socket já que achou uma porta
    except:
        # contin o programa
        # pass
        print("[-] Port closed " + str(port))




targets = input("[*] Digite os alvos dos ips(separados por ,): ") # digita
ports = int(input("[*] Quantas portas você quer scan?: "))

if ',' in targets:
    print(termcolor.colored("[+] Múltiplos alvos", 'green'))
    for ip_addr in targets.split(','):
        # strip remove espaços em branco
        scan(ip_addr.strip(' '), ports)

else:
        scan(targets, ports)