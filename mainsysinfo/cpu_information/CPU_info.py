import psutil
import logging


class CPU:

    @staticmethod
    def cpu_freq():
        try:
            '''Information about CPU freq'''
            freq = ("CPU freq stats : {}".format(psutil.cpu_freq(percpu=True)))
            return freq
        except Exception as e:
            logging.exception(e)

    @staticmethod
    def cpu_count():
        try:
            '''Information about amount of cores'''
            count = ("Amount of cores : {}".format(psutil.cpu_count(True)))
            return count
        except Exception as e:
            logging.exception(e)

    @staticmethod
    def cpu_stats():
        try:
            '''Information of CPU stats'''
            stats = ("CPU stats : {}".format(psutil.cpu_stats()))
            return stats
        except Exception as e:
            logging.exception(e)

    @staticmethod
    def cpu_show_all():
        """Show all stats method"""
        all_stats = ("{} \n{} \n{}".format(CPU.cpu_stats(), CPU.cpu_count(), CPU.cpu_freq()))
        # CPU.cpu_stats()
        # CPU.cpu_count()
        # CPU.cpu_freq()
        return all_stats


if __name__ == "__main__":
    CPU_stats = CPU()
    CPU_stats.cpu_show_all()
