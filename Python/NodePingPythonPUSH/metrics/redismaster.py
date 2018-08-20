# -*- coding: utf-8 -*-

"""
Collects who the Redis Master is at the time
REQUIRES: python-redis v2.9 or higher
"""

from redis.sentinel import Sentinel
from . import _utils

################################## USER DEFINED VARIABLES ################

# Name of the Redis master server
REDIS_MASTER = ""
# IP of sentinel to query
SENTINEL_IP = ""
# Port Redis Sentinel is running on
PORT = ""

##########################################################################


def main(system, logger):
    """
    Returns the IP address of the current Redis Master
    """

    sentinel = Sentinel([(SENTINEL_IP, PORT)], socket_timeout=0.1)
    master = sentinel.discover_master(REDIS_MASTER)

    return _utils.report(master[0])
