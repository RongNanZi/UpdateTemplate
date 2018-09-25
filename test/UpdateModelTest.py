from UpdateModel import *

data = pd.read_csv('C:\\Users\\Lenovo\\PycharmProjects\\UpdateTemplate\\data\\sms_template.csv')

def add_pre_end(s):
    o_s = s['origin']
    if o_s[0] != '$':
        o_s = '$'+o_s
    if not o_s.endswith('#'):
        o_s += '#'
    s['origin'] = o_s

    o_s = s['template']
    if o_s[0] != '$':
        o_s = '$' + o_s
    if not o_s.endswith('#'):
        o_s += '#'
    s['template'] = o_s
    return s

data = data.apply(add_pre_end, axis=1)
data.to_csv('C:\\Users\\Lenovo\\PycharmProjects\\UpdateTemplate\\data\\sms_template.csv',index=False)