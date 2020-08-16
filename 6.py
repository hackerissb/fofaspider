import requests
import re
import base64
import base64
import io
import time
import sys
def cj_c(url):
    str_url = base64.b64encode(url.encode('utf-8'))
    cookies = dict(
        cookies_are='Hm_lvt_9490413c5eebdadf757c2be2c816aedf=1597044555,1597044623,1597044891,1597052235; _fofapro_ars_session=ffaa9370b4c7c0a6a4f31e68a9c08c37; referer_url=%2Fresult%3Fqbase64%3DMjIy; Hm_lpvt_9490413c5eebdadf757c2be2c816aedf=1597062020')
    a = 'https://classic.fofa.so/result?page=' + '1' + '&qbase64=' + str(str_url, ('utf-8'))
    print(a)
    rul = '">(.*?)</a> '

    c = requests.get(a, cookies=cookies)
    d = c.text

    sss = str(re.findall(rul, d)[15])
    iu = sss.rfind('>')

    ii = int(sss[iu:].replace('>', ''))
    print('一共有' + str(ii) + '页')
    for i in range(0, ii):

        cookies = dict(
            cookies_are='Hm_lvt_9490413c5eebdadf757c2be2c816aedf=1597044555,1597044623,1597044891,1597052235; _fofapro_ars_session=ffaa9370b4c7c0a6a4f31e68a9c08c37; referer_url=%2Fresult%3Fqbase64%3DMjIy; Hm_lpvt_9490413c5eebdadf757c2be2c816aedf=1597062020')
        a = 'https://classic.fofa.so/result?page=' + str(i) + '&qbase64=' + str(str_url, ('utf-8'))
        print(a)
        c = requests.get(a, cookies=cookies)
        d = c.text
        while 'Retry later' in d:
            time.sleep(10)
            cookies = dict(
                cookies_are='Hm_lvt_9490413c5eebdadf757c2be2c816aedf=1597044555,1597044623,1597044891,1597052235; _fofapro_ars_session=ffaa9370b4c7c0a6a4f31e68a9c08c37; referer_url=%2Fresult%3Fqbase64%3DMjIy; Hm_lpvt_9490413c5eebdadf757c2be2c816aedf=1597062020')
            a = 'https://classic.fofa.so/result?page=' + str(i) + '&qbase64=' + str(str_url, ('utf-8'))
            print(a)
            c = requests.get(a, cookies=cookies)
            d = c.text
        rule = r'<a target="_blank" href="(.*?)">'
        slotList = re.findall(rule, d)

        for i in range(len(slotList)):

            s = slotList[i]

            if 'beta.fofa.so' not in s:
                if 'host' not in s:
                    if 'beian.miit.gov.cn' not in s:
                        list = []
                        list.append(slotList[i])
                        print(list)
                        with open('ipw.txt', 'a') as f:
                            for item in list:
                                f.write("%s\n" % item)
if __name__ == '__main__':
    url='博彩'
    cj_c(url)