import sys
from QT.QQ import *
from parsed import *
from QT.ListView import ListView

s = '您的账单日期是2018年12月10日，话费余额20元，消费30元#'
t_s = '{nonsence:1-2}日期是{账单日期：2-20}，话费余额{余额：2-10}，消费{消费：2-10}#'
kv = parsed(s, t_s)

#m_list = ListModel(kv)
#v_list = ListView(kv)
qq = QQ(kv)

app = QApplication(sys.argv)
qq.show()
app.exec_()