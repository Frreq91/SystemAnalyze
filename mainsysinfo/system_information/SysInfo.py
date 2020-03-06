import logging
import platform
import psutil
import re
import socket
import uuid


class SysInfo:

    @staticmethod
    def get_system_information():
        try:
            '''Display all information about this PC'''
            PlatformInformation = {'platform': platform.system(), 'platform-release': platform.release(),
                                   'platform-version': platform.version(), 'architecture': platform.machine(),
                                   'hostname': socket.gethostname(),
                                   'ip-address': socket.gethostbyname(socket.gethostname()),
                                   'mac-address': ':'.join(re.findall('..', '%012x' % uuid.getnode())),
                                   'processor': platform.processor(), 'processor cores': str(psutil.cpu_count()),
                                   'ram': str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"}
            return PlatformInformation
        except Exception as e:
            logging.exception(e)


if __name__ == "__main__":
    logging.debug(SysInfo.get_system_information())
