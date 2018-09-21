import re

s = '您的账单日期是2018年12月10日，话费余额20元，消费30元#'
t_s = '{nonsence}日期是{账单日期}，话费余额{话费余额}，消费{本月消费}#'

def parsedSliod(s):
    wanted =[]

    re_pattern = '{(?P<key_type>.*?)}'
    finds = re.findall(re_pattern, s)

    if finds:
        return finds
    else:
        print('illeagal template')
    return wanted




def parsed(text, t):

    keys = parsedSliod(t)
    t = re.sub('{(?P<key_type>.*?)}', '', t)
    values = []
    flag = True
    i = 0
    j = 0
    value_s_idx = -1
    while i < len(text):

        if text[i] == t[j] :
            if flag == False :
                values.append(text[value_s_idx:i])

                flag = True
            i += 1
            j +=1
        else:
            if flag:
                value_s_idx = i
                flag = False

            i += 1

    wanted = list(zip(keys, values))

    return wanted


print(parsed(s, t_s))