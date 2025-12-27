import socket
import time
from channel import transmit # channel.py의 손실 구현 함수 불러오기

HOST = "127.0.0.1"
PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 소켓 객체 생성 및 IPv4, UDP 설정

for i in range(20):
    packet = f"packet-{i}"
    result = transmit(packet, loss_rate=0.2, delay_ms=500) # 500ms 지연 후, 20% 확률로 손실되는 패킷 전송

    if result: # 손실되지 않았나?
        sock.sendto(result.encode(), (HOST, PORT))
        print(f"Sent: {packet}") # 전송 성공
    else:
        print(f"Lost: {packet}") # 손실

    time.sleep(0.5) # 0.5초 지연