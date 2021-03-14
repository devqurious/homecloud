#!/usr/bin/python3

from kubernetes import client, config
import os

# Retrieve the API
config.load_kube_config(config_file="/home/ubuntu/.kube/config")
api = client.CoreV1Api()

pod_list = api.list_namespaced_pod("minecraft")
for pod in pod_list.items:
    print("%s" % pod.metadata.name)
    os.system('sudo kubectl -n minecraft --address 0.0.0.0 port-forward ' + pod.metadata.name + ' 25565:25565')
    