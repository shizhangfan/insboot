import urllib.request as request
import time
import datetime

def test_request():
    url = 'https://www.baidu.com'
    req = request.Request(url)
    http_handler = request.HTTPHandler()
    opener = request.build_opener(http_handler)
    response = opener.open(req, timeout=60)
    response_content = response.read().decode('utf-8')

    print('>>>>>>>>>>>>>>>>>>>>')
    print(response_content)

def test_get_phone():
    API_BASE_URL = 'http://api.fxhyd.cn/UserInterface.aspx'
    API_TOKEN = '00662039b612335469fc69b4410c1e9d9e7548129e01'
    YM_PROJECT_CODE = '455'
    url = '{0}?action=getmobile&token={1}&itemid={3}&excludeno=170.171.180&' \
          'timestamp={2}'.format(API_BASE_URL, API_TOKEN, time.mktime(datetime.datetime.now().timetuple()), YM_PROJECT_CODE)
    
    req = request.Request(url)
    http_handler = request.HTTPSHandler()
    opener = request.build_opener(http_handler)
    response = opener.open(req, timeout=15)
    response_content = response.read().decode('utf-8')
    print(response_content)
    if response_content.find('success') > 0:
        phone = response_content.split('|')[1]
        return phone
    else:
        return "error"

def main():
    # test_request()
    test_str = '1success|13610997874'
    # phone = test_get_phone()
    print(test_str.find('success'))
    if test_str.find('success') >= 0:
        print('yes')
        print(test_str.split('|')[1])
    else:
        print('no')
    # print(phone)

if __name__ == "__main__":
    main()