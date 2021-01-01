import subprocess

def uvicorn_service():
    logfile = ""
    app = ""
    srcdir = ""
    subprocess.call(["nohup uvicorn core:app &> nohup2.out &"], shell=True)

uvicorn_service()
