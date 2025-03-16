# 解密程序 dic.py
import base64
import os
import tkinter as tk
from tkinter import filedialog, ttk
import time

class DictionaryApp:
    def __init__(self):
        self.data = {}
        
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("单词查询器")
        
        # 设置窗口大小
        self.root.geometry("900x600")
        
        # 设置窗口背景色
        self.root.configure(bg="#f0f0f0")
        
        # 创建控件
        self.create_widgets()
    
    def create_widgets(self):
        # 当前词典文件标签和按钮
        tk.Label(self.root, text="当前词典文件:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.current_file_label = tk.Label(self.root, text="无", bg="#f0f0f0")
        self.current_file_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        select_file_btn = tk.Button(self.root, text="选择字典文件", command=self.load_file, bg="#4CAF50", fg="white", relief=tk.FLAT)
        select_file_btn.grid(row=0, column=2, padx=10, pady=10)
        
        # 进度条
        self.progress_bar_load = ttk.Progressbar(self.root, mode="determinate", length=300)
        self.progress_bar_load.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        
        # 输入单词标签、文本框和查询按钮
        tk.Label(self.root, text="输入单词:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(self.root, textvariable=self.search_var, width=30)
        search_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        search_entry.bind("<Return>", lambda event: self.do_search())  # 绑定回车键事件
        search_btn = ttk.Button(self.root, text="查询", command=self.do_search)
        search_btn.grid(row=1, column=2, padx=10, pady=10)
        
        # 查询进度条
        self.progress_bar_search = ttk.Progressbar(self.root, mode="determinate", length=300)
        self.progress_bar_search.grid(row=1, column=1, padx=10, pady=10, sticky="e")
        
        # 结果显示区域
        result_frame = ttk.LabelFrame(self.root, text="查询结果", labelanchor="n")
        result_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        
        self.result_text = tk.Text(result_frame, height=20, width=100, bg="white")
        self.result_text.pack(padx=10, pady=10)
        
        # 按钮框架
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="e")
        
        # 复制结果按钮
        copy_btn = tk.Button(button_frame, text="复制结果", command=self.copy_result, bg="#2196F3", fg="white", relief=tk.FLAT)
        copy_btn.pack(side=tk.RIGHT, padx=5)
        
        # 清空结果按钮
        clear_btn = tk.Button(button_frame, text="清空结果", command=self.clear_result, bg="#f44336", fg="white", relief=tk.FLAT)
        clear_btn.pack(side=tk.RIGHT, padx=5)
        
        # 设置列权重，使控件可以自适应窗口大小
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
    
    def xor_crypt(self, data, key):
        return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])
    
    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Dict Files", "*.dict")])
        if not file_path:
            return
        
        # 更新当前词典文件标签
        self.current_file_label.config(text=os.path.basename(file_path))
        
        # 读取密钥
        key_path = os.path.splitext(file_path)[0] + ".key"
        with open(key_path, 'rb') as f:
            key = base64.b64decode(f.read())
        
        # 解密数据
        with open(file_path, 'rb') as f:
            encrypted = base64.b64decode(f.read())
            decrypted = self.xor_crypt(encrypted, key).decode('utf-8')
        
        # 解析数据
        self.data.clear()
        total_rows = len(decrypted.split('\n'))
        for i, row in enumerate(decrypted.split('\n')):
            self.progress_bar_load["value"] = (i + 1) / total_rows * 100
            self.root.update_idletasks()
            cells = row.split(',', 3)
            if len(cells) >= 4:
                word = cells[0].strip()
                self.data[word.lower()] = cells
        self.progress_bar_load["value"] = 0
    
    def do_search(self):
        self.result_text.delete(1.0, tk.END)
        word = self.search_var.get().strip().lower()
        
        # 显示查询进度条
        self.progress_bar_search["mode"] = "determinate"
        self.progress_bar_search["value"] = 0
        
        # 模拟查询延迟
        for i in range(101):
            self.progress_bar_search["value"] = i
            self.root.update_idletasks()
            time.sleep(0.01)
        
        result = self.data.get(word)
        
        if result:
            formatted_result = (
                f"单词: {result[0]}\n"
                f"英式音标: 英 [{result[1]}]\n"
                f"美式音标: 美 [{result[2]}]\n"
                f"词性#翻译: \n"
                f"{result[3].replace('#', '\n', 1)}"
            )
            self.result_text.insert(tk.END, formatted_result)
        else:
            self.result_text.insert(tk.END, "未找到该单词")
    
    def copy_result(self):
        result = self.result_text.get(1.0, tk.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(result)
    
    def clear_result(self):
        self.result_text.delete(1.0, tk.END)

if __name__ == "__main__":
    app = DictionaryApp()
    app.root.mainloop()