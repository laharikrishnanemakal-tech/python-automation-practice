def check_server_health(server):
    if server["cpu"] > 80 or server["memory"] > 80:
        return "UNHEALTHY"
    return "HEALTHY"


servers = [
    {"name": "server1", "cpu": 45, "memory": 60},
    {"name": "server2", "cpu": 92, "memory": 85},
    {"name": "server3", "cpu": 30, "memory": 40}
]

for server in servers:
    status = check_server_health(server)
    print(f"\nServer: {server['name']}")
    print(f"Status: {status}")

    if server["cpu"] > 80:
        print(f"High CPU usage: {server['cpu']}%")

    if server["memory"] > 80:
        print(f"High memory usage: {server['memory']}%")