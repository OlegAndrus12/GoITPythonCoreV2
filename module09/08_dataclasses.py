from dataclasses import dataclass, field


# @dataclass auto-generates __init__, __repr__, __eq__ from the field declarations
@dataclass
class Endpoint:
    path: str
    method: str = "GET"
    auth_required: bool = False


@dataclass
class ServiceConfig:
    host: str
    port: int
    endpoints: list = field(default_factory=list)  # mutable default must use field()

    def add_endpoint(self, endpoint):
        self.endpoints.append(endpoint)

    def base_url(self):
        return f"http://{self.host}:{self.port}"


config = ServiceConfig("localhost", 8000)
config.add_endpoint(Endpoint("/users"))
config.add_endpoint(Endpoint("/admin", auth_required=True))
config.add_endpoint(Endpoint("/users", "POST", True))

print(config.base_url())
print(config)

for ep in config.endpoints:
    print(ep)

print("--------------------")

# equality is based on field values (not object identity)
e1 = Endpoint("/users")
e2 = Endpoint("/users")
print(e1 == e2)    # True  — unlike plain classes where this would be False
