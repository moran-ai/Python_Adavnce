import subprocess

# 通过文件句柄的方式传参
f = open('1.txt')
# PIPE不能传给系统命令 subprocess有一个接口Popen可以传参给系统命令
run_cmd = subprocess.run('python', stdin=f, stdout=subprocess.PIPE, shell=True)
print(run_cmd.stdout)
f.close()