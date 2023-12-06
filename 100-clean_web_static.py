#!/usr/bin/python3
""" This is a Fabric script (based on the file 3-deploy_web_static.py) that deletes
    out-of-date archives, using the function do_clean: """

from fabric.api import *
from datetime import datetime
from os.path import exists

def do_clean(number=0):
    """Deletes out-of-date archives"""

    if int(number) < 0:
        number = 0
    else:
        number = int(number)

    # Get the list of all archives
    archives = sorted(run("ls -1 /data/web_static/releases/").split())

    # Delete archives in versions folder
    local("ls -1t versions | tail -n +{} | xargs -I {} rm versions/{}".format(number + 1, "{}"))

    # Delete archives in releases folder on both web servers
    for archive in archives[:-number]:
        run("rm -rf /data/web_static/releases/{}".format(archive))

    print("Cleaned up old archives!")
