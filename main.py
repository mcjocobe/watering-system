from machine import Pin
import network
import time
from secrets import ssid, password
import socket


def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    counter = 0
    while not wlan.isconnected() and wlan.status() >= 0 and counter < 30:
        print("Waiting to connect to {}:", ssid)
        time.sleep(1)
        counter = counter + 1
    print("Connected to wifi, ", ssid)
    status = wlan.ifconfig()
    print("ip = " + status[0])


relay = Pin(20, Pin.OUT)
connect_wifi(ssid, password)
# Open socket
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)
except OSError as e:
    print(f" >> ERROR: {e}")

finally:
    print(" >> Connection closed.")
    s.close()
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
print("listening on", addr)


while True:
    try:
        cl, addr = s.accept()
        print("client connected from", addr)
        request = cl.recv(1024)
        print(request)

        request = str(request)
        relay_on = request.find("/relay1/on")
        relay_off = request.find("/relay1/off")
        print("Relay on = " + str(relay_on))
        print("Relay off = " + str(relay_off))

        if relay_on >= 6:
            print("Realy on")
            relay.value(0)
            stateis = "LED is ON"
        if relay_off >= 6:
            print("Realy off")
            relay.value(1)
            stateis = "LED is OFF"

        cl.send("HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
        cl.close()
    except OSError as e:
        print(f" >> ERROR: {e}")

    finally:
        # appearantly, context managers are currently not supported in MicroPython, therefore the connection is closed manually
        cl.close()
        print(" >> Connection closed.")
