from abc import ABC, abstractmethod

# ABC = nominal subtyping: a class satisfies the interface only if it
# explicitly inherits from the ABC and implements all abstract methods.
#
# Trying to instantiate a class with unimplemented abstract methods raises TypeError.


class HealthCheckable(ABC):
    @abstractmethod
    def health_check(self):
        pass


class DatabasePool(HealthCheckable):
    def __init__(self, host):
        self.host = host
        self._connected = True

    def health_check(self):
        status = "ok" if self._connected else "down"
        return {"service": "database", "host": self.host, "status": status}


class CacheClient(HealthCheckable):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def health_check(self):
        return {"service": "cache", "host": self.host, "status": "ok", "latency_ms": 2}


class ExternalAPI(HealthCheckable):
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def health_check(self):
        return {"service": self.name, "url": self.url, "status": "ok"}


# this class forgets to implement health_check
class BrokenService(HealthCheckable):
    pass


def run_health_checks(services):
    report = {}
    for service in services:
        report[type(service).__name__] = service.health_check()
    return report


services = [
    DatabasePool("db.prod.internal"),
    CacheClient("redis.prod.internal", 6379),
    ExternalAPI("payments", "https://api.payments.com"),
]

for name, result in run_health_checks(services).items():
    print(f"{name}: {result}")

print("--------------------")

# isinstance works because of explicit inheritance
for s in services:
    print(f"{type(s).__name__}: isinstance HealthCheckable → {isinstance(s, HealthCheckable)}")

print("--------------------")

# ABC enforces the contract at instantiation time
try:
    broken = BrokenService()
except TypeError as e:
    print(f"BrokenService: {e}")
