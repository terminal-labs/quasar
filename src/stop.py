import subprocess

port = 8000
try:
    cmd = 'lsof -t -i:{0}'.format(port)
    pid = subprocess.check_output(cmd, shell=True)
    print(int(pid))
except subprocess.CalledProcessError:
    print("not found")

isKilled = subprocess.check_output('kill -9 {0}'.format(str(int(pid))), shell=True) if pid else None
