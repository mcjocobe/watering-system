import time
import socket

watering_client = "192.168.1.109"


def set_relay(watering_client, state):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"/relay1/{state}")
    try:
        s.connect((watering_client, 80))
        s.send(bytes(f"/relay1/{state}\n", "UTF-8"))
        print("Message sent to: ", watering_client)
    except Exception as e:
        print("something went wrong", e)
    finally:
        print("close")
        s.close


def main():
    set_relay(watering_client, "on")


main()
