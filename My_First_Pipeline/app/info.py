import os
import socket
import subprocess

def get_container_info():
    container_name = socket.gethostname()
    host_name = subprocess.getoutput("hostname")
    image_name = subprocess.getoutput("cat /proc/1/cgroup | grep 'docker' || echo 'unknown'")
    container_ip = subprocess.getoutput("hostname -I | awk '{print $1}'")

    return {
        "container_name": container_name,
        "host_name": host_name,
        "image_name": image_name,
        "container_ip": container_ip
    }

if __name__ == "__main__":
    import json
    print(json.dumps(get_container_info()))
