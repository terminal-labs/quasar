import os
import pathlib
import subprocess

def srcpgk_service_restapi():
    port = "5000"
    apppath = "core:app"
    logfile = "nohup3.out"

    shell = "bash"
    srvapp = "uvicorn"
    os.chdir(str(pathlib.Path(__file__).parent.absolute()))
    subprocess.call([f"{shell} -c 'nohup {srvapp} --port {port} {apppath} &> {logfile} &'"], shell=True)

srcpgk_service_restapi()
