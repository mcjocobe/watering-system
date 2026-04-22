import datetime
import json
import time
import socket
import requests

watering_client = "192.168.1.245"
schedule_file_name = "schedule.json"


def set_relay(target_ip, state):
    print(f"/relay1/{state} on {target_ip}", target_ip + f"/relay1/{state}")
    headers = {"Accept": "*/*"}
    try:
        response = requests.get(target_ip + f"/relay1/{state}", headers=headers, timeout=10, proxies={"http": None, "https": None})
        print("Message sent to: ", target_ip)
    except Exception as e:
        print("something went wrong", e)
    finally:
        print("close")


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
