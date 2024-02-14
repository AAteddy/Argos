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

        print("Connected to the server!")

        # Here, you can perform actions on the server or retrieve information

        # Fetch system information
        cpu_percentage = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        io_counters = psutil.disk_io_counters()

        # Fetch network information
        hostname = socket.gethostname()
        open_ports = [x[1] for x in socket.getaddrinfo(hostname, None)]

        # Print or use the fetched information as needed
        print("CPU Percentage:", cpu_percentage)
        print("Memory Info:", memory_info)
        print("IO Counters:", io_counters)
        print("Hostname:", hostname)
        print("Open Ports:", open_ports)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SSH connection when done
        client.close()


# Replace these with your actual server details
hostname = "6ef5dd0f56d0.ca3bcf03.alx-cod.online"
port = 22  # Default SSH port
username = "6ef5dd0f56d0"
password = "9428affc18a667f0b64c"

connect_to_server(hostname, port, username, password)
