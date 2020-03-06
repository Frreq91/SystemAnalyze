import psutil
import logging


class CPU:

    @staticmethod
    def cpu_freq():
        try:
            '''Information about CPU freq'''
            print("CPU freq stats : {}".format(psutil.cpu_freq(percpu=True)))
        except Exception as e:
            logging.exception(e)

    @staticmethod
    def cpu_count():
        try:
            '''Information about amount of cores'''
            print("Amout of cores : {}".format(psutil.cpu_count(True)))
        except Exception as e:
            logging.exception(e)

    @staticmethod
    def cpu_stats():
        try:
            '''Information of CPU stats'''
            print("CPU stats : {}".format(psutil.cpu_stats()))
        except Exception as e:
            logging.exception(e)

    @staticmethod
    def cpu_show_all():
        """Show all stats method"""
        CPU.cpu_stats()
        CPU.cpu_count()
        CPU.cpu_freq()


if __name__ == "__main__":
    CPU_stats = CPU()
    CPU_stats.cpu_show_all()
