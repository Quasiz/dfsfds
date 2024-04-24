import sys
import socket
import time
import threading

def send_udp(ip, port, packet_size):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = b"A" * packet_size  # Create a packet of specified size filled with 'A's
        while True:
            sock.sendto(data, (ip, port))
    except Exception as e:
        print("Error:", e)

def main():
    if len(sys.argv) != 5:
        print("Usage: python udp_sender.py <ip> <port> <duration> <packet_size>")
        return

    ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = float(sys.argv[3])
    packet_size = int(sys.argv[4])

    try:
        duration = float(duration)
    except ValueError:
        print("Duration should be a number (in seconds)")
        return

    print(f"Sending UDP requests to {ip}:{port} for {duration} seconds with packet size {packet_size} bytes...")

    thread = threading.Thread(target=send_udp, args=(ip, port, packet_size))
    thread.start()

    time.sleep(duration)

    print("Stopping...")
    thread.join()

if __name__ == "__main__":
    main()
