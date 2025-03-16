# 加密程序 encrypt_dict.py
import csv
import os
import random
import base64
import tkinter as tk
from tkinter import filedialog

def xor_crypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def encrypt_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return
    
    # 读取CSV数据
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 4:
                data.append(row)
    
    # 生成随机密钥（16字节）
    key = bytes([random.randint(0, 255) for _ in range(16)])
    
    # 加密数据
    data_str = '\n'.join([','.join(row) for row in data])
    encrypted = xor_crypt(data_str.encode('utf-8'), key)
    
    # 保存文件
    base_path = os.path.splitext(file_path)[0]
    with open(f"{base_path}.dict", 'wb') as f:
        f.write(base64.b64encode(encrypted))
    with open(f"{base_path}.key", 'wb') as f:
        f.write(base64.b64encode(key))
    
    tk.messagebox.showinfo("成功", "加密完成！")

root = tk.Tk()
root.title("CSV加密工具")
tk.Button(root, text="选择CSV文件并加密", command=encrypt_file).pack(padx=20, pady=20)
root.mainloop()