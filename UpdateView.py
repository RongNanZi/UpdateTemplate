from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import askstring, askinteger, askfloat

class UpdateView(Frame):
    def __init__(self, m_data, master=None):
        super().__init__(master)
        self.model_data = m_data
        self.create_ui()

    def create_ui(self):

        #原句
        self.origin_s_ui = Text(height=2, width=100)
        self.origin_s_ui.insert(END, self.model_data.origin_s)
        self.origin_s_ui.pack()

        self.sence_ui = ttk.Combobox(values=list(self.model_data.all_sence.keys()))
        self.sence_ui.pack()

        label_ui = ttk.Label(text='算法生成的模板')
        label_ui.pack()

        self.w_template_ui = Text(height=2, width=100)
        self.w_template_ui.insert(END, self.model_data.mis_template)
        self.w_template_ui.pack()

        label_t_ui = ttk.Label(text='您的修改')
        label_t_ui.pack()

        self.t_template_ui = Text(height=2, width=100)
        self.t_template_ui.insert(END, self.model_data.mis_template)
        self.t_template_ui.pack()

        self.test_result_ui = Text(height=7, width=100)
        self.test_result_ui.pack()


        self.test_ui = ttk.Button(text='测试模板生成', command=lambda : self.test_tempalate())
        self.test_ui.pack()
        self.save_ui = ttk.Button(text='模板入库', command=lambda: self.save2file())
        self.save_ui.pack()




    def test_tempalate(self):
        new_template = self.t_template_ui.get(1.0, END).strip()
        self.model_data.tru_template = new_template
        result = self.model_data.get_result()
        self.test_result_ui.delete(1.0, 'end')
        for k,v in result.items():
            self.test_result_ui.insert('end', '{} : {}\n'.format(k, v))


    def is_success(self, find_keys, should_keys):
        flag = True
        for item in find_keys:
            if item in should_keys:
                continue
            else:
                text = askstring('入库错误', '【{}】关键字不是标准关键字,非要入库,请输入关键字'.format(item))
                if text == None:
                    return False
                elif text != item:
                    text = askstring('入库错误', '【{}】关键字不是标准关键字,重新输入，最后一次机会'.format(item))
                if text == None or(text!=item):
                    return False

        for item in should_keys:
            if item in find_keys:
                continue
            else:
                text = askstring('入库错误', '【{}】关键字不是标准关键字,非要入库,请输入关键字'.format(item))
                if text == None:
                    return False
                elif text != item:
                    text = askstring('入库错误', '【{}】关键字重新输入，最后一次机会'.format(item))
                if text == None or(text!=item):
                    return False
        return True




    def save2file(self):
        '''
        模板入库
        :return:
        '''
        #get sence
        sence = self.sence_ui.get()
        true_temp = self.t_template_ui.get(1.0,END).strip()
        if sence != '通用场景':
            should_keys = self.model_data.all_sence[sence]
            find_keys = [item.split(' : ')[0] for item in self.test_result_ui.get(1.0,END).strip().split('\n')]
            if not self.is_success(find_keys, should_keys):
                return

        tk.messagebox.showinfo('入库结果',self.model_data.save(true_temp))
        m = self.model_data.next_model()
        if m == 'finish':
            tk.messagebox.showinfo('入库结果','所有数据都录入')
        else:
            self.model_data = m









