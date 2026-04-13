from ncclient import manager

# Router connection details
router = {
    "host": "192.168.56.101",   # Change if needed (NetLab vs local VM)
    "port": 830,
    "username": "cisco",
    "password": "cisco",
    "hostkey_verify": False
}

# NETCONF filter to retrieve interface configuration
filter_xml = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <GigabitEthernet>
        <name>1.10</name>
      </GigabitEthernet>
    </interface>
  </native>
</filter>
"""

# Connect and retrieve configuration
with manager.connect(**router) as m:
    response = m.get_config(source="running", filter=filter_xml)
    print(response)