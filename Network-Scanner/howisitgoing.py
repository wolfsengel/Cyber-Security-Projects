import socket

def escanear_puertos(ip, puertos):
    for puerto in puertos:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        resultado = s.connect_ex((ip, puerto))
        if resultado == 0:
            print(f'Puerto {puerto} abierto en {ip}')
        else:
            print(f'Puerto {puerto} cerrado en {ip}')
        s.close()

# Ejemplo de uso
ip = '127.0.0.1'
puertos = [21, 22, 80, 443, 3306]
escanear_puertos(ip, puertos)

def escanear_puertos_automaticamente(ip):
    for puerto in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        resultado = s.connect_ex((ip, puerto))
        if resultado == 0:
            print(f'Puerto {puerto} abierto en {ip}')
        else:
            print(f'Puerto {puerto} cerrado en {ip}')
        s.close()

# Ejemplo de uso con ip del usuario
ip = input('Introduce la ip a escanear: ')
escanear_puertos_automaticamente(ip)
