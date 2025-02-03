from dataclasses import dataclass

@dataclass
class VapixServer:
    host: str
    port: int

@dataclass
class VapixUserCredencials:
    username: str
    password: str

@dataclass
class VapixConfig:
    server: VapixServer
    credencials: VapixUserCredencials
