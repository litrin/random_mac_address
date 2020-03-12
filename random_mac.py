import os
import random
import sys


def get_random_mac():
    tmp = []
    for i in range(6):
        value = random.randint(0x1, 0xFF)

        if i == 1 and ((value & 1) == 1):
            value -= 1
        tmp.append(value)

    return ":".join(["%X" % i for i in tmp])


def set_networkconfig_file(device, mac_address):
    filename = "/etc/sysconfig/network-scripts/ifcfg-%s" % device
    cmd = "echo MACADDR=%s >> %s"(mac_address, filename)

    status = os.system(cmd)
    return status


def enable_interface(device, mac_address):
    cmd = "ip link set %s address %s" % (device, mac_address)

    status = os.system(cmd)
    return status


if __name__ == "__main__":
    eth = sys.argv[1]

    mac = get_random_mac()
    enable_interface(device=eth, mac_address=mac)
    set_networkconfig_file(device=eth, mac_address=mac)
