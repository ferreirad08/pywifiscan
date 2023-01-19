from pywifiscan import get_interface, scan_networks

# Getting the default Network Interface
iface = get_interface()

networks = scan_networks(iface)

print(networks)
# {
#     'networkName0': -70,
#     'networkName1': -75,
#     ...
#     'networkNameN': -91
# }
