#!/usr/bin/python3
""" This python script distributes an archive to web servers,
using the function do_deploy"""
import logging
from os.path import exists
from fabric.api import run, put, env

# Configure logging
logging.basicConfig(level=logging.INFO)

env.hosts = ["34.229.49.169", "54.162.223.76"]
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """Deployes the archive to the webserver"""
    if not exists(archive_path):
        logging.error("Archive file does not exist")
        return False

    full_name = archive_path.split("/")[1]
    file_name = archive_path.split("/")[1].split(".")[0]

    # Transfer the archive file to the server
    try:
        put(archive_path, "/tmp/{}".format(full_name))
    except Exception as e:
        logging.error("Failed to transfer archive file: %s", e)
        return False

    # Remove the existing directory
    result = run("sudo rm -rf /data/web_static/releases/{}/".format(file_name))
    if result.failed:
        logging.error("Failed to remove existing directory")
        logging.error("Command: %s", result.command)
        logging.error("Return code: %s", result.return_code)
        logging.error("Stdout: %s", result.stdout)
        logging.error("Stderr: %s", result.stderr)
        return False

    # Create a new directory
    result = run("sudo mkdir -p /data/web_static/releases/{}/".format(file_name))
    if result.failed:
        logging.error("Failed to create new directory")
        logging.error("Command: %s", result.command)
        logging.error("Return code: %s", result.return_code)
        logging.error("Stdout: %s", result.stdout)
        logging.error("Stderr: %s", result.stderr)
        return False

    # Extract the archive file into the new directory
    result = run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(full_name, file_name))
    if result.failed:
        logging.error("Failed to extract archive file")
        logging.error("Command: %s", result.command)
        logging.error("Return code: %s", result.return_code)
        logging.error("Stdout: %s", result.stdout)
        logging.error("Stderr: %s", result.stderr)
        return False

    logging.info("Deployment successful")
