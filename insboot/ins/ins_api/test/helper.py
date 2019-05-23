import re
import random


def generate_uuid():
    return re.sub('[xy]', lambda x: to_hex(random.randint(0, 15)), 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx')


def to_hex(num):
    """
    :type num: int
    :rtype: str
    """
    my_dic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    if num < 10:
        return str(num)
    else:
        return my_dic[num]


if __name__ == "__main__":
    print(generate_uuid())
