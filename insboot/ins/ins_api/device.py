import json
import hashlib


class Device(object):

    def __init__(self, username):
        if not username:
            raise Exception("username blank error")
        if not isinstance(username, str):
            raise Exception("username must be instance of string")
        self.username = username

        with open("devices.json") as data_f:
            self.devices = json.load(data_f)

    @property
    def id(self):
        """
        Android device ID
        :return:
        """
        return 'android-{0!s}'.format(self.md5[:16])

    @property
    def md5(self):
        """
        md5
        :return:
        """
        return hashlib.md5(self.username.encode("utf-8")).hexdigest()

    @property
    def md5int(self):
        return int(int(self.md5, 32) / 10e32)

    @property
    def info(self):
        line = self.devices[self.md5int % len(self.devices)]
        info = {
            "manufacturer": line[0],
            "device": line[1],
            "model": line[2]
        }
        return info

    @property
    def api(self):
        return 18 + (self.md5int % 5)

    @property
    def release(self):
        return ['4.0.4', '4.3.1', '4.4.4', '5.1.1', '6.0.1', '7.0.0', '8.0.2', '9.0'][self.md5int % 8]

    @property
    def phone_chipset(self):
        return ['qualcommsnapdragon855', 'samsungexynos9820', 'hisiliconkirin980', 'samsungexynos9810',
                'qualcommsnapdragon845', 'hisiliconkirin970', 'samsungexynos9610', 'samsungexynos8890octa',
                'hisiliconkirin960', 'hisiliconkirin960s', 'qualcommsnapdragon835', 'qualcommsnapdragon712',
                'samsungexynos8895octa', 'samsungexynos7885'][self.md5int % 14]

    @property
    def payload(self):
        payload = {}
        payload.manufacturer = self.info.get('manufacturer')
        payload.model = self.info.get('model')
        payload.android_version = self.api
        payload.android_release = self.release
        return payload

    @property
    def dpi(self):
        return ['801', '577', '576', '538', '515', '424', '401', '373'][self.md5int % 8]

    @property
    def resolution(self):
        return ['3840x2160', '1440x2560', '2560x1440', '1440x2560', '2560x1440', '1080x1920',
                '1080x1920', '1080x1920'][self.md5int % 8]

    @property
    def language(self):
        return 'en_US'

    def get_user_agent(self, version=None):
        agent = ["{}/{}".format(self.api, self.release), '{0!s}dpi'.format(self.dpi), self.resolution,
                 self.info.get("manufacturer"), self.info.get('model'), self.info.get('device'), self.language]
        return self.instagram_agent_template('; '.join(agent), version or 'v1')

    @staticmethod
    def instagram_agent_template(agent, version):
        return 'Instagram {} Android {}'.format(version, agent)


if __name__ == "__main__":
    device = Device("shizf")
    # print("md5: {0!s}".format(device.md5))
    # print(int(device.md5, 32))
    # print(int(int(device.md5, 32) / 10e32))
    # print("md5int: {}".format(device.md5int))
    # print("info:{}".format(device.md5int % len(device.devices)))
    # print(device.info)
    # print("api: {}".format(device.api))
    # print("release")
    # print(device.release)
    # print(device.get_user_agent())
