import platform
import subprocess
import os
from pythonping import ping
from dotenv import load_dotenv


load_dotenv()


def pinging_host(host_ip):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host_ip]

    return subprocess.call(command) == 0


if __name__ == '__main__':
    """
    don't forget about the executor.py line 236 
    if self.verbose:
        print(value, file=self.output)
    """
    # r = pinging_host('192.100.1.108')
    # if r:
    #     print("done")
    # else:
    #     print("can't connect")
    hosts = os.getenv("HOSTS").split(" ")
    for host in hosts:
        response = ping(host, verbose=True, count=2, timeout=5)
        r = response.stats_packets_returned
        print(r)
