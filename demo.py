import requests

file = open("ip.txt", "r")

lists = file.readlines()
i = 0
for fields in lists:
    try:
        i=i+1


        c = str(lists[i])


        a = requests.get(c, verify=False)

        list1 = []
        list1.append(str(lists[i].replace("\n", ""))+"状态码"+str(a.status_code))

        print(list1)

        with open('ips.txt', 'a') as f:
            for item in list1:
                f.write("%s\n" % item)
    except:
        del lists[i]
        i=i+1


