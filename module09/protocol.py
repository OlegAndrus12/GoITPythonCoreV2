from typing import Protocol, runtime_checkable

# Protocol = structural subtyping: a class satisfies a Protocol if it has
# the right methods/attributes — no explicit inheritance required.
#
# With ABC:      class EmailClient(Notifier): ...   ← must opt in
# With Protocol: class EmailClient: ...             ← just needs the right shape


@runtime_checkable          # enables isinstance() checks at runtime
class HealthCheckable(Protocol):
    def health_check(self): ...


# None of these classes know about HealthCheckable — they just happen to have the method

class DatabasePool:
    def __init__(self, host):
        self.host = host
        self._connected = True

    def health_check(self):
        status = "ok" if self._connected else "down"
        return {"service": "database", "host": self.host, "status": status}


class CacheClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def health_check(self):
        return {"service": "cache", "host": self.host, "status": "ok", "latency_ms": 2}


class ExternalAPI:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def health_check(self):
        return {"service": self.name, "url": self.url, "status": "ok"}


# this class does NOT satisfy the protocol — no health_check method
class AppConfig:
    debug = False
    version = "1.0.0"


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

# isinstance works at runtime thanks to @runtime_checkable
for s in services:
    print(f"{type(s).__name__}: implements HealthCheckable → {isinstance(s, HealthCheckable)}")

cfg = AppConfig()
print(f"AppConfig: implements HealthCheckable → {isinstance(cfg, HealthCheckable)}")

print("--------------------")

for name, result in run_health_checks(services).items():
    print(f"{name}: {result}")
