# aggregation: the outer object REFERENCES an inner object that exists independently
# the inner object can be shared across multiple outer objects and outlives them


class Developer:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def info(self):
        return f"{self.name} ({self.role})"


class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, developer):
        self.members.append(developer)

    def roster(self):
        return [m.info() for m in self.members]


alice = Developer("Alice", "Backend")
bob = Developer("Bob", "Frontend")
carol = Developer("Carol", "DevOps")

team_phoenix = Team("Phoenix")
team_phoenix.add(alice)
team_phoenix.add(bob)

team_atlas = Team("Atlas")
team_atlas.add(carol)
team_atlas.add(alice)   # Alice is on both teams — she exists independently

print(team_phoenix.roster())   # ['Alice (Backend)', 'Bob (Frontend)']
print(team_atlas.roster())     # ['Carol (DevOps)', 'Alice (Backend)']

# Developer objects are created outside — they can be passed around freely
