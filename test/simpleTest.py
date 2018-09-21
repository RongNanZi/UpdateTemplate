import tkinter as tk
from tkinter.simpledialog import askstring, askinteger, askfloat
import pandas as pd
data = pd.DataFrame([{'wanted':"{nonsence}日期是{账单月份}，话费余额{话费余额}，消费{本月消费}#"}])
data.to_csv('template.csv', index=False)
# 接收一个整数
def print_integer():
    res = askinteger("Spam", "Egg count", initialvalue=12 * 12)
    print(res)


# 接收一个浮点数
def print_float():
    res = askfloat("Spam", "Egg weight\n(in tons)", minvalue=1, maxvalue=100)
    print(res)


# 接收一个字符串
def print_string():
    res = askstring("Spam", "Egg label")
    print(res)


root = tk.Tk()

tk.Button(root, text='取一个字符串', command=print_string).pack()
tk.Button(root, text='取一个整数', command=print_integer).pack()
tk.Button(root, text='取一个浮点数', command=print_float).pack()

root.mainloop()
