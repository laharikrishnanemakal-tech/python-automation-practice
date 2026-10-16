from server_health_check import check_server_health


def test_healthy_server():
    server = {"name": "server1", "cpu": 45, "memory": 60}
    assert check_server_health(server) == "HEALTHY"


def test_high_cpu_server():
    server = {"name": "server2", "cpu": 95, "memory": 50}
    assert check_server_health(server) == "UNHEALTHY"


def test_high_memory_server():
    server = {"name": "server3", "cpu": 40, "memory": 90}
    assert check_server_health(server) == "UNHEALTHY"