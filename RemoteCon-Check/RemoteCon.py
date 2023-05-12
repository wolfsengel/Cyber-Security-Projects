import socket

def check_for_rdp_connections():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 3388))
        s.listen(1)
        print("Listening for RDP connections...")
        conn, addr = s.accept()
        print("RDP connection from:", addr)

check_for_rdp_connections()
