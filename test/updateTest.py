from tkinter import *
from UpdateView import *
from UpdateModel import *
import pandas as pd

s = '您的账单日期是2018年12月10日，话费余额20元，消费30元#'
t_s = '{nonsence}日期是{账单日期}，话费余额{余额}，消费{消费}#'
csv = pd.DataFrame()
csv.loc[0, 'origin'] = s
csv.loc[0, 'template'] = t_s
csv.loc[0, 'sence'] = '通用'
csv.to_csv('mis_temp.csv',  index=False)

data = UpdateModel('C:\\Users\\Lenovo\\PycharmProjects\\UpdateTemplate\\test\\mis_temp.csv', 'template.csv')

root = Tk()
app = UpdateView(master=root, m_data = data)
app.mainloop()
