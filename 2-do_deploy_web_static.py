#!/usr/bin/python3
""" This is a Fabric script (based on the file 1-pack_web_static.py) that distributes..
    ..an archive to your web servers, using the function do_deploy: """

from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['35.237.166.125', '54.167.61.201']

def do_deploy(archive_path):
    """ distributes an archive to my web servers """
    if not exists(archive_path):
        print(f"Error: Archive {archive_path} not found.")
        return False

    try:
        # Extract necessary information
        filename = archive_path.split('/')[-1]
        no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
        tmp = "/tmp/" + filename

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, tmp)

        # Uncompress the archive to the folder /data/web_static/releases/
        # <archive filename without extension> on the web server
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))

        # Remove the uploaded archive from the web server
        run("rm {}".format(tmp))

        # Move the contents to the desired location
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current on the
        # web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        run("ln -s {}/ /data/web_static/current".format(no_tgz))

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Error deploying: {e}")
        return False
