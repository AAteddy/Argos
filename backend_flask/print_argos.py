from argos import connect_to_server

server_metrics = connect_to_server(
    "62468bd2f6a3.e336d92f.alx-cod.online", 22, "62468bd2f6a3", "3bca7fb8e251461e68e2"
)

cpu = server_metrics["cpu_info"]
Host = server_metrics["host_name"]

print(cpu)
print(Host)
