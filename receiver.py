import socket

HOST = "127.0.0.1"
POST = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 소켓 객체 생성 및 IPv4, UDP 설정

sock.bind((HOST, POST)) // HOST와 POST에 연결

print("receiver started")

while True:
    data, addr = sock.recvfrom(1024) # 1024 바이트 데이터 수신 
    print(f"Received: {data.decode()} from {addr}") # 바이트로 전송된 패킷을 문자열화 후, 수신자 기록