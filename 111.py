import csv
import os

file_list = os.listdir("excel")

#print(file_list)

i = 0
for ff in file_list:
    try:
        f = open("excel/" + ff, 'r', encoding='euc-kr')
        rdr = csv.reader(f)
        for line1 in rdr:
            #print(line1)
            break
    except:
        f = open("excel/" + ff, 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line1 in rdr:
            #print(line1)
            break
    ls = []
    for line1 in rdr:
        pp = True
        for line2 in ls:
            check = True
            for s1 in range(len(line2)):
                #print(line1[s1], end="\t")
                #print(line2[s1])
                if s1 == 10 or s1 == 9:
                    #print(line1[s1][:-2])
                    if line1[s1][:-2] == line2[s1][:-2]:# and line1[s1-1][:-2] == line2[s1-1][:-2]:
                        continue
                if line1[s1] != line2[s1]:
                    check = False
                    break
            #check = false
            if check:
                pp = False
                break
        if pp:
            ls.append(line1)
    #for a in ls:
        #print(a)
    f.close()

    f1 = open("asdf/" + ff, 'w', encoding='euc-kr')
    f1.write('"device_serial","device_scode","온도","습도","조도","움직임","최종움직임 koKR","Co2","TVOC","측정일시 koKR","등록일시 koKR","보류"\n')
    for a in ls:
        f1.writelines(",".join(a))
        f1.write("\n")
    f1.close()
    #print(1)
    i += 1
    print(str(i) + "/" + str(len(file_list)))
print('end')