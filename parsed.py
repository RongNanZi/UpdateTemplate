import re

s = '$您的账单日期是2018年12月10日，话费余额20元，消费30元#'
t_s = '${nonsence}日期是{账单日期}，话费余额{话费余额}，消费{本月消费}#'

def parsedSliod(s):
    wanted =[]

    re_pattern = '{(?P<key_type>.*?)}'
    finds = re.findall(re_pattern, s)

    if finds:
        return finds
    else:
        print('illeagal template')
    return wanted

def pased_parsed(text, t):

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

def parsed(text, t):
    '''
    给出文本和文本模板提取key-value对

    :param text: string, start with '$" end with '#'
    :param t: string,
    :return: list tuple object
    '''
    origing_text = text

    keys = parsedSliod(t)
    #在模板中用 ‘{}’替换掉关键字，并作为分隔符
    t = re.sub('{(?P<key_type>.*?)}', '{}', t)
    values = []
    t_pattern = t.split('{}')
    # idxs是一个（匹配到部分开始位置，匹配到部分结束位置）的list
    idxs = []
    last_idx = 0
    for t_p  in t_pattern:
        if t_p == '#':
            idxs.append((len(origing_text)-1, len(origing_text)-1))
            break
        idx = text.find(t_p)
        new_idx = idx + len(t_p)
        idxs.append((last_idx+idx, last_idx+new_idx))
        last_idx = idxs[-1][-1]
        text = text[new_idx:]
    # 在前一个匹配部分结束位置和当前匹配到的部分来作为提取到的value值
    for i in range(len(idxs)-1):
        s_idx = idxs[i][-1]
        e_idx = idxs[i+1][0]
        values.append(origing_text[s_idx:e_idx])

    wanted = list(zip(keys, values))

    return wanted

print(parsed(s, t_s))