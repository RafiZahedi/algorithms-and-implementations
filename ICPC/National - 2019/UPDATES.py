def process(servers, clients):
    class Module:
        def __init__(self, name, version):
            self.name = name
            self.version = version

        def __lt__(self, other):
            # Compare name
            result = self.name.compare(other.name)
            if result != 0:
                return result < 0

            mine = self.explode(self.version)
            his = self.explode(other.version)

            # Compare each part of their version
            for i in range(min(len(mine), len(his))):
                result = mine[i] - his[i]
                if result != 0:
                    return result < 0

            # Compare the one with fewer version parts
            return len(mine) < len(his)

        @staticmethod
        def explode(version):
            parts = version.split(".")
            return [int(part) for part in parts]

        def __str__(self):
            return f"{self.name}.v{self.version}"

    server_modules = []
    for identifier in servers.split(","):
        i = identifier.rfind(".v")
        server_modules.append(Module(identifier[:i], identifier[i + 2:]))

    client_modules = []
    for identifier in clients.split(","):
        i = identifier.rfind(".v")
        client_modules.append(Module(identifier[:i], identifier[i + 2:]))

    updating_modules = []

    for client in client_modules:
        for server in server_modules:
            if client.name == server.name and client < server:
                updating_modules.append(server)
                server_modules.remove(server)

    updating_modules.sort()

    return ",".join(map(str, updating_modules))


# Example usage
server_modules_str = "a.v1,b.v2.0.1,c.v1.1,d.v0.0,e.v5.0.9,f.v0.0.0.20191010101010"
client_modules_str = "a.v1,c.v1.1.0.20191010101010,e.v5.1,f.v0.0.0.20191010101011"

output = process(server_modules_str, client_modules_str)
print(output)
