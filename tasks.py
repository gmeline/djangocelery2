from celery_config import app
import subprocess

#Ping
@app.task
def ping_ip(ip):
    command = f"ping -c 1 {ip}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode()

@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y
