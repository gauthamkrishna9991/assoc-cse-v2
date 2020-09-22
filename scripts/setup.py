#!/usr/bin/python3
# Setting up System Libraries.

import platform, subprocess
from typing import List

def parse_releasefile(releasefile: List[str]):
    final_retn = {}
    for line in releasefile:
        line: str
        k, v = line.strip().split("=")
        final_retn[k] = v
    return final_retn


# If the system is Linux:
if platform.system() == "Linux":
    # Find out the distro first.
    try:
        f = open("/etc/os-release", "r")
        releasefile = parse_releasefile(f.readlines(200))
        # If the platform is RPM-Based
        if releasefile['ID'] == "fedora" or releasefile['ID'] == "centos" or releasefile['ID'] == "rhel":
            subprocess.run("./initialize/rpm.sh")
        #else if is Debian-Based
        elif releasefile['ID'] == "ubuntu" or releasefile['ID'] == "debian":
            subprocess.run("./initialize/debian.sh")
        else:
            print("Install the requirements given in docs/REQUIREMENTS.md")
    except FileNotFoundError as fnferr:
        print(fnferr)
        print("os-release file not found. Please install the files you see in docs/REQUIREMENTS.md")