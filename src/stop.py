import subprocess

port = 8000

def get_pids():
    pids = None
    try:
        cmd = 'lsof -t -i:{0}'.format(port)
        pid = subprocess.check_output(cmd, shell=True)
        pid = pid.decode("utf-8")
        if "\n" in pid:
            pids = pid.split("\n")
        else:
            pids = [pid]
    except subprocess.CalledProcessError:
        print("not found")

    if pids:
        pids.remove("")
    return pids

pids = get_pids()
if pids:
    for pid in pids:
        subprocess.check_output('kill -9 {0}'.format(pid), shell=True)
