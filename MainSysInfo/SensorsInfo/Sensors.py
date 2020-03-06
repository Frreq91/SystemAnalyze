import psutil
import time
import datetime
import logging


class SensorsInfo:

    @staticmethod
    def sec2hours():
        """Counting time"""
        secs = psutil.sensors_battery().secsleft
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d" % (hh, mm, ss)

    @staticmethod
    def battery_info():
        try:
            """Create new txt file"""
            with open("Batteryinfo.txt", 'a') as batteryinfo:
                while True:
                    """Check battery state"""
                    battery = psutil.sensors_battery()

                    """Create new file and save it"""
                    batteryinfo.write("Charge = {} | Time left {} | Current time {} \n".format(battery.percent
                                                , SensorsInfo.sec2hours().replace("-", "")
                                                , datetime.datetime.now().strftime("%H:%M:%S")))
                    batteryinfo.flush()
                    time.sleep(60)
        except Exception as e:
            logging.exception(e)


if __name__ == '__main__':
    SensorsInfo.battery_info()
