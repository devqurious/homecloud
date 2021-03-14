from kubernetes import client, config
from kubernetes.stream import stream
import pihole as ph

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config(config_file="/home/ubuntu/.kube/config")

v1 = client.CoreV1Api()

print("Listing pods with their IPs:")
ret = v1.list_namespaced_pod(namespace='default', label_selector='release=pihole')
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    print(i.spec.hostname)

    name = i.metadata.name

    resp = v1.read_namespaced_pod(name=name, namespace=i.metadata.namespace)

    exec_command = [
    'sqlite3',
    '/etc/pihole/gravity.db',
    "update 'group' set enabled = 1 where name = 'Restricted'"
    ]

    resp = stream(v1.connect_get_namespaced_pod_exec, name, i.metadata.namespace,
              command=exec_command,
              stderr=True, stdin=False,
              stdout=True, tty=False)


    print("============================ Cleanup %s: ============================\n%s\n" % (name, resp if resp else "<no output>"))


    # pihole = ph.PiHole(i.status.pod_ip)
    # # version = pihole.getVersion()
    # # print(version)

    # ret = pihole.authenticate("admin")
    # pihole.add("regex_black", "(\.|^)youtube\.com$")
    # pihole.add("regex_black", "(\.|^)scratch\.mit\.edu$")
    # pihole.add("regex_black", "(\.|^)code\.org$")
