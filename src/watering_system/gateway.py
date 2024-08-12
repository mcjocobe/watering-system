import datetime
import json
import time
import socket

watering_client = "192.168.1.109"
schedule_file_name = "schedule.json"


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


def delete_schedule(watering_schedule):
    with open(schedule_file_name, "w") as file:
        json.dump(data, file)
    return watering_schedule


def wait_for_schedule():
    watering_time = 5
    with open(schedule_file_name, "r") as file:
        data = json.load(file)
    schedules = list(data.items())
    while True:
        if watering_schedule < time.time():
            set_relay(watering_client, "on")
            time.sleep(watering_time)
            set_relay(watering_client, "off")
            watering_schedule = delete_schedule()
            break


def add_schedule_system(date_str, relay_id):

    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    timestamp = int(datetime.datetime.timestamp(date))
    data = {relay_id: timestamp}
    json_data = json.dumps(data)
    with open(schedule_file_name, "w") as file:
        file.write(json_data)
    return json_data


def main():
    # set_relay(watering_client, "off")
    # wait_for_schedule()
    print(add_schedule_system("2024-04-14 15:30", "relay1"))


main()
