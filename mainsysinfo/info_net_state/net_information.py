import psutil
import datetime
import time
import logging


class NetworkInfo:

    @staticmethod
    def upload_download_information():
        try:
            '''Creating or opne new txt file'''
            with open("NetworkStats.txt", "a") as network:

                '''First stats'''
                start_upload = (psutil.net_io_counters().bytes_sent / 1024)
                start_download = (psutil.net_io_counters().bytes_recv / 1024)
                while True:
                    '''Counting Network stats like upload and download in kB'''
                    end_upload = (psutil.net_io_counters().bytes_sent / 1024)
                    end_download = (psutil.net_io_counters().bytes_recv / 1024)
                    up = end_upload - start_upload
                    down = end_download - start_download
                    start_upload = end_upload
                    start_download = end_download
                    time.sleep(0.75)

                    '''Add stats to txt file'''
                    network.writelines('Upload : {:0.2f} kB | Download {:0.2f} kB | Time : {} \n'.format(up
                                        , down, datetime.datetime.now().strftime("%H:%M:%S")))
                    network.flush()

        except Exception as e:
            logging.exception(e)


if __name__ == '__main__':
    NetworkInfo.upload_download_information()
