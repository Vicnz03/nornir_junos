from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_junos.tasks.junos_get import junos_get
from nornir.core.plugins.connections import ConnectionPluginRegister
from nornir_junos.connections import nornir_junos
ConnectionPluginRegister.register("nornir_junos", nornir_junos)
nr = InitNornir(
    runner={
        "plugin": "threaded",
        "options": {
            "num_workers": 100,
        },
    },
    inventory={
        "plugin": "SimpleInventory",
        "options": {
            "host_file": "inventory/hosts.yaml"
        },
    },
)

results = nr.run(
    task=junos_get, commands=["show system uptime"]
)
print_result(results)
