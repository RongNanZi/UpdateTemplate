import tkinter as tk
from tkinter.simpledialog import askstring, askinteger, askfloat
import pandas as pd
data = pd.DataFrame([{'wanted':"{nonsence}日期是{账单月份}，话费余额{话费余额}，消费{本月消费}#"}])
data.to_csv('template.csv', index=False)
