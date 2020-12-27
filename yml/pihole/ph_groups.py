#!/usr/bin/python3

from kubernetes import client, config
from kubernetes.stream import stream
from datetime import datetime
import pihole as ph
import sys
import argparse

# Process commang line args
parser = argparse.ArgumentParser("Pihole Group Control")
parser.add_argument("groupName", help="Name of group", type=str)
parser.add_argument("enable", help="Enable or disable a group (0 disable, 1 enable)", type=int)
args = parser.parse_args()
enable = args.enable
groupName = args.groupName

# Retrieve the API
config.load_kube_config(config_file="/home/ubuntu/.kube/config")
api = client.CoreV1Api()

# Find the IP address(es) of the pihole pods
ret = api.list_namespaced_pod(namespace='default', label_selector='release=pihole')
for i in ret.items:
    #print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    name = i.metadata.name
    resp = api.read_namespaced_pod(name=name, namespace=i.metadata.namespace)
    exec_command = [
    'sqlite3',
    '/etc/pihole/gravity.db',
    "update 'group' set enabled = " + str(enable) + " where name = '" + groupName + "'"
    ]

    resp = stream(api.connect_get_namespaced_pod_exec, name, i.metadata.namespace,
              command=exec_command,
              stderr=True, stdin=False,
              stdout=True, tty=False)

    now = datetime.today()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("%s:%s:%s:%s --%s \n" % (dt_string, name, str(enable), groupName, resp if resp else "Updated!"))
