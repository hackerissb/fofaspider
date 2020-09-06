import requests
import re
import base64
import time


global cookie
global headers


with open('cookie.txt', 'r') as f:
   cookie=f.read()
print(cookie)
def cj_c(url):

    str_url = base64.b64encode(url.encode('utf-8'))
    cookies = dict(
        cookies_are=cookie)
    a = 'https://classic.fofa.so/result?page=' + '1' + '&qbase64=' + str(str_url, ('utf-8'))
    print(a)
    rul = '">(.*?)</a> '

    c = requests.get(a, cookies=cookies)
    d = c.text


    sss = str(re.findall(rul, d)[15])
    iu = sss.rfind('>')

    ii = int(sss[iu:].replace('>', ''))
    print('一共有' + str(ii) + '页')
    for i in range(5, ii):

        cookies = dict(
            cookies_are=cookie)
        a = 'https://classic.fofa.so/result?page=' + str(i) + '&qbase64=' + str(str_url, ('utf-8'))
        print(a)
        c = requests.get(a, cookies=cookies)
        d = c.text

        time.sleep(7)
        while 'Retry later' in d:
            time.sleep(20)
            cookies = dict(
                cookies_are=cookie)
            a = 'https://classic.fofa.so/result?page=' + str(i) + '&qbase64=' + str(str_url, ('utf-8'))
            print(a)
            c = requests.get(a, cookies=cookies)
            print(c.content)
            d = c.text
            print(d)
        rule = r'<a target="_blank" href="(.*?)">'
        slotList = re.findall(rule, d)

        for i in range(len(slotList)):

            s = slotList[i]
            print(s)
            if 'beta.fofa.so' not in s:
                if 'host' not in s:
                    if 'beian.miit.gov.cn' not in s:
                        list = []
                        list.append(slotList[i])
                        print(list)
                        with open('soap.txt', 'a') as f:
                            for item in list:
                                f.write("%s\n" % item)
if __name__ == '__main__':
    url='''"asmx?wsdl"'''
    cj_c(url)
