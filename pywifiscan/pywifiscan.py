from subprocess import check_output


def get_interface() -> str:
    try:
        return check_output("route | grep default | awk 'NR==1 {print $NF}'", shell=True)\
            .decode("utf-8").replace("\n", "")
    except:
        return ""


def scan_networks(iface) -> dict:
    try:
        lines = check_output(f"sudo iwlist {iface} scan | grep -Po '(?<=(ESSID:\")).*(?=\")|(?<=(level=)).*(?= dBm)'", shell=True)\
            .decode("utf-8").splitlines()

        networks = {}

        for i in range(1, len(lines), 2):
            networks[lines[i]] = int(lines[i - 1])

        return networks
    except:
        return {}
