import random
import time

def transmit(packet, loss_rate=0.1, delay_ms=300):
    if random.random() < loss_rate: # 0~1사이의 랜덤 값 < 손실 확률
        return None # 손실 처리

    time.sleep(delay_ms / 1000)
    return packet
