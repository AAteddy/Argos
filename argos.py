import paramiko

def fetch_metrics(hostname, port, username, password):
    try:
        # Create an SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)

        # Execute commands to fetch metrics
        commands = [
            "top -b -n 1",        # CPU and memory
            "df -h",              # Disk space
            "netstat -i",         # Network interfaces
        ]

        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            print(f"Output of '{command}':")
            print(stdout.read().decode())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SSH connection when done
        client.close()

# Replace these with your actual server details
hostname = 'your_server_ip'
port = 22  # Default SSH port
username = 'your_username'
password = 'your_password'

fetch_metrics(hostname, port, username, password)