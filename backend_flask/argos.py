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

        # print("CPU Percentage:", cpu_percentage)
        # print("Memory Info:", memory_info)
        # print("Disk Percentage:", disk_info)
        # print("IO Counters:", io_counters)
        # print("Hostname:", hostname)
        # print("Open Ports:", open_ports)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SSH connection when done
        client.close()


# Replace these with your actual server details
# hostname = "62468bd2f6a3.e336d92f.alx-cod.online"
# port = 22  # Default SSH port
# username = "62468bd2f6a3"
# password = "3bca7fb8e251461e68e2"

# connect_to_server(hostname, port, username, password)
