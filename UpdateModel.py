
import pandas as pd
from parsed import *



class UpdateModel(object):
    def __init__(self, f_Path, save_path):
        self.all_sence = {'账单提醒':['账单月份', '话费余额', '本月消费'],\
                          '缴费成功':['充费渠道','缴费金额'],\
                          '积分查询':['截止时间','积分剩余'],\
                          '通用场景':[]}
        self.data = pd.read_csv(f_Path)
        self.data = self.clean_data()
        self.idx = 0
        self.origin_s = self.data.loc[0, 'origin']
        self.mis_template = self.data.loc[0, 'template']
        self.sence = self.data.loc[0, 'sence']
        self.tru_template = self.mis_template
        self.template_lib_path = save_path

    def is_already_find(self):
        '''
        判断当前self.origin_s句子是不是已经可以在模板库中被识别
        :return: boolean, True or False
        '''
        if self.sence != '通用场景' and (self.sence in self.all_sence.keys()):
            template = pd.read_csv(self.template_lib_path)
            for i in template.index:
                t = template.loc[i, 'wanted']
                result = parsed(s, t)
                result = set(result)
                stan_result = set(self.all_sence[self.sence])
                if result == stan_result:
                    return True
        return False

    def next_model(self):
        '''
        取下一个被解析的句子
        :return:
        '''
        if self.idx == self.data.shape[0]-1:
            return "finish"
        self.idx += 1
        self.origin_s = self.data.loc[self.idx, 'origin']

        if self.is_already_find():
            return self.next_model()
        else:
            self.mis_template = self.data.loc[self.idx, 'template']
            return self

    def get_result(self):
        all_values = parsed(self.origin_s, self.tru_template)
        wanted = {}
        wanted.update({item[0]:item[1] for item in all_values if item[0]!='nonsence'})
        return wanted

    def save(self, template):
        #save template to file
        t_data = pd.read_csv('template.csv')
        t_data.loc[t_data.index[-1]+1] = {'wanted':template}
        t_data = t_data.drop_duplicates(['wanted'])
        try:
            t_data.to_csv('template.csv', index=False)
        except Exception as e:
            return e

        return "OK"

    def clean_data(self):
        '''
        对输入所有新类型的句子去掉非“nonsence"场景，去掉相似度95%以上句子
        :return:
        '''
        def drop_non(s):
            t = s['template']
            t = re.sub('{[^nonsence]}', '', t)
            s['tempalte'] = t
            return s
        data = self.data.apply(drop_non, axis=1)
        data = data.drop_duplicates(['template'])
        return data
