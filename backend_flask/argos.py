import paramiko
import psutil
import socket


def connect_to_server(hostname, port, username, password):
    try:
        # Create an SSH client
        client = paramiko.SSHClient()

        # Automatically add the server's host key (this is insecure, see comments below)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote server
        client.connect(hostname, port, username, password)

        # Here, you can perform actions on the server or retrieve information

        # Fetch system information
        cpu_percentage = psutil.cpu_percent()
        memory_percentage = psutil.virtual_memory()[2]
        disk_percentage = psutil.disk_usage("/")[3]

        # io_counters = psutil.disk_io_counters()

        # # Fetch network information
        # hostname = socket.gethostname()
        # open_ports = [x[1] for x in socket.getaddrinfo(hostname, None)]

        # Print or use the fetched information as needed
        server_metrics = {
            "cpu_info": cpu_percentage,
            "memory_info": memory_percentage,
            "disk_info": disk_percentage,
        }
        return server_metrics

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SSH connection when done
        client.close()
