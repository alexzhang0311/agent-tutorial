# server_health_check_tool.py

import paramiko
from collections import defaultdict
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from langchain_core.tools.base import ArgsSchema
from typing import Optional

class ServerHealthCheckInput(BaseModel):
    ip: str = Field(description="The IP address of the server")
    username: str = Field(description="The username for SSH login, default is 'app'", default="app")


class ServerHealthCheckTool(BaseTool):
    name: str = "System Health Check Tool"
    description: str = "A tool to perform server resource inspection via SSH using public key authentication."
    args_schema: Optional[ArgsSchema] = ServerHealthCheckInput
    return_direct: bool = True
    private_key_path: str = "/data/app/.ssh/id_rsa"


    def _run(self, ip, username):
        stats_dict = defaultdict(str)
        client = self.ssh_connect(host=ip, username=username, private_key_path=self.private_key_path)
        
        if client is not None:
            stats_dict['System Information'] = self.get_remote_system_info(client)
            stats_dict['CPU Info'] = self.get_remote_cpu_info(client)
            stats_dict['Memory Info'] = self.get_remote_memory_info(client)
            stats_dict['Disk Info'] = self.get_remote_disk_info(client)
            stats_dict['Network Info'] = self.get_remote_network_info(client)

            client.close()
        
        return stats_dict

    def ssh_connect(self, host, username, private_key_path):
        """ Connect to the remote host over SSH using a private key """
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
            client.connect(hostname=host, username=username, pkey=private_key)
            return client
        except Exception as e:
            print(f"Failed to connect {host} due to: {str(e)}")
            return None

    def run_remote_command(self, ssh_client, command):
        """ Execute a command remotely and return its output """
        stdin, stdout, stderr = ssh_client.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()

    def get_remote_system_info(self, ssh_client):
        output, _ = self.run_remote_command(ssh_client, 'uname -a; uptime -p')
        return output.strip()

    def get_remote_cpu_info(self, ssh_client):
        output, _ = self.run_remote_command(ssh_client, "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\([0-9.]*\)%* id.*/\\1/' | awk '{print 100 - $1\"%\"}'")
        return output.strip()

    def get_remote_memory_info(self, ssh_client):
        output, _ = self.run_remote_command(ssh_client, "free -mh")
        lines = output.split('\n')
        mem_line = [line for line in lines if line.startswith('Mem:')][0].split()
        memory_total = mem_line[1]
        memory_used = mem_line[2]
        return f"Memory Used: {int(memory_used) * 100 // int(memory_total)}% of {memory_total}"

    def get_remote_disk_info(self, ssh_client):
        output, _ = self.run_remote_command(ssh_client, "df -h | grep '^/'")
        parts = output.split()
        total, used, available, percent = parts[1], parts[2], parts[3], parts[4]
        return f"Disk Usage: {percent} of {total}"

    def get_remote_network_info(self, ssh_client):
        output, _ = self.run_remote_command(ssh_client, "cat /proc/net/dev | grep ': '| awk '{totalrx+=$2; totaltx+=$10} END{printf \"Network Data Sent: %.2f MB | Received: %.2f MB\", totaltx/(1024**2), totalrx/(1024**2)}'")
        return output.strip()
