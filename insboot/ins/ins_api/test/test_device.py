from ..device import Device

if __name__ == "__main__":
    device = Device("shizf")
    print("md5: {0!s}".format(device.md5))
    print("md5int: {0!d}".format(device.md5int))
