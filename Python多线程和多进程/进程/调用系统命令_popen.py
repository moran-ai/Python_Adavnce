import subprocess

# 使用popen传参数
popen = subprocess.Popen('python', stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
popen.stdin.write('print("hello word")\n'.encode('utf-8'))  # 转为字节数据
popen.stdin.write('import os'.encode('utf-8'))
popen.stdin.close()

out = popen.stdout.read().decode('gbk')
popen.stdout.close()
print(out)
