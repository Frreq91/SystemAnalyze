import threading
import logging
import sys
import datetime
import time

from SystemInformation.SysInfo import SysInfo
from InfoNetState.NetInformation import NetworkInfo
from SensorsInfo.Sensors import SensorsInfo


def main():
    time_end = int
    loop_state = True
    while loop_state:
        try:
            sec_to_end = int(input("Set time in sec : "))
            time_start = datetime.datetime.now()
            time_end = time_start + datetime.timedelta(seconds=sec_to_end)
            loop_state = False
        except Exception as e:
            logging.exception(e)

    sys_info_func()
    t_net = threading.Thread(target=network_func, daemon=True)
    t_net.start()
    t_battery = threading.Thread(target=battery_func, daemon=True)
    t_battery.start()
    t_time = threading.Thread(target=time_checking_func(time_end), daemon=True)
    t_time.start()


def time_checking_func(time_to_end):
    while True:
        time.sleep(1)
        if time_to_end.strftime("%Y/%b/%d %H:%M:%S") == datetime.datetime.now().strftime("%Y/%b/%d %H:%M:%S"):
            sys.exit("Monitoring Finished, all threads closed")
        else:
            pass


def sys_info_func():
    SysInformation = SysInfo.get_system_information()
    for key, value in SysInformation.items():
        print(key + ' : ' + value)


def network_func():
    NetworkInfo.upload_download_information()


def battery_func():
    SensorsInfo.battery_info()


if __name__ == '__main__':
    main()
