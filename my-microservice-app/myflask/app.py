import os
import sys
import subprocess
import re
import platform
import pytz
import socket
from datetime import datetime


from flask import Flask

app = Flask(__name__)


def get_install_packeges(packege_name):
    p = {}
    instPack = subprocess.run('pip freeze', shell=True,
                              stdout=subprocess.PIPE).stdout.decode('utf-8')
    instPack = re.findall(r"[\w']+.*", instPack)
    for i in range(len(instPack)):
        instPack[i] = instPack[i].split('==')
    for iP in instPack:
        p.update({iP[0]: iP[1]})
    return p[packege_name]


def get_family_name():
    return subprocess.run('uname -o', shell=True,
                   stdout=subprocess.PIPE).stdout.decode('utf-8')


def get_date_created():
    return os.getenv('DATE_CREATED')


def get_host_and_ip():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return (host_ip, host_name)

def get_container_life_time():
    return subprocess.run('ps -o etime | head -n2', shell=True,
                              stdout=subprocess.PIPE).stdout.decode('utf-8').split()[1]


@app.route("/")
def content():
    page = '<html><body><h1>'
    page += 'TASK 6'
    page += '</h1>'
    page += f'Python version {sys.version[:5]}, <br /> '
    page += f'\nFlask version {get_install_packeges("Flask")}, <br />'
    page += f'\nOS name {os.name} {platform.system()}, Release Version: {platform.release()},<br />' \
        f'Family Name: {get_family_name()},<br /> '
    page += f'\n Kernel Version {platform.version()},<br /> '
    page += f'\n Date Create {get_date_created()}<br />, '
    page += f'Page generation date/time in zones UTC0: {datetime.now(pytz.utc)}, <br />'  \
        f'Page generation date/time in zones Europe/Minsk: {datetime.now(pytz.timezone("Europe/Minsk"))} '
    page += f'System Host Name, IP address {socket.gethostname()}, {socket.gethostbyname(socket.gethostname())}<br />'
    page += f'Student name {os.getenv("NAME_CREATOR")}<br />'
    page += f'Container Life time: {get_container_life_time()}<br />'
    page += '</body></html>'

    return page


def parse_date_bash(date_null):

    date_arr = date_null.split()
    date_date = date_arr[0].split('-')
    date_time = date_arr[1].split(':')
    dateCteated = datetime(int(date_date[0]), int(date_date[1]), int(date_date[2]),
                          int(date_time[0]), int(date_time[1]), int(date_time[2]))

    return dateCteated


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))  # port 5000 is the default