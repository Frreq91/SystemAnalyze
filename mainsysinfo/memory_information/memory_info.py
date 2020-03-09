import psutil
import logging


class Memory:

    @staticmethod
    def memory_virtual():
        try:
            memory_var = ("Memory stats : {}".format(psutil.virtual_memory()))
            return memory_var
        except Exception as e:
            logging.exception(e)


if __name__ == "__main__":
    Memory.memory_virtual()
