from namizun_core import database
from random import randint
from time import sleep
from namizun_core.monitor import get_network_io
from namizun_core.udp import multi_udp_uploader


def get_network_usage():
    upload, download = get_network_io()
    difference = download - upload / (randint(
        database.get_cache_parameter('coefficient') * 7, database.get_cache_parameter('coefficient') * 13) / 10)
    if difference < 1:
        return 1
    elif difference > 100000000 * database.get_cache_parameter('speed'):
        return 100000000 * database.get_cache_parameter('speed')
    return difference


while True:
    database.set_parameters_to_cache()
    if database.get_cache_parameter('running'):
        count = randint(70, 140)
        size = get_network_usage()
        while count >= 0:
            count -= multi_udp_uploader(size)
    sleep(randint(50, 200))
