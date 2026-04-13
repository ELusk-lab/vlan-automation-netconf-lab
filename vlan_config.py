from ncclient import manager

# Router connection details
router = {
    "host": "192.168.56.101",   # Change if using NetLab (e.g., 192.168.56.101 or 192.168.56.x)
    "port": 830,
    "username": "cisco",
    "password": "cisco",
    "hostkey_verify": False
}

# NETCONF configuration payload
netconf_config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <GigabitEthernet>
        <name>1.10</name>
        <description>VLAN10_SUBINTERFACE</description>
        <encapsulation>
          <dot1Q>
            <vlan-id>10</vlan-id>
          </dot1Q>
        </encapsulation>
        <ip>
          <address>
            <primary>
              <address>192.168.10.1</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
      </GigabitEthernet>
    </interface>
  </native>
</config>
"""

# Connect to router and push configuration
with manager.connect(**router) as m:
    response = m.edit_config(target="running", config=netconf_config)
    print("GigabitEthernet1.10 successfully configured for VLAN 10")