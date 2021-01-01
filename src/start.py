import subprocess

subprocess.call(["nohup uvicorn core:app &> nohup2.out &"], shell=True)
print("done")
