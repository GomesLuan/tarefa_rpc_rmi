import sys

import Pyro5.api

# utilizar este campo quando rodar na nuvem
IP = "3.87.17.216"
PORTA_NS = 443

# buscando a URI do objeto remoto no name server
monit = Pyro5.api.Proxy(f"PYRONAME:monitor@{IP}:{PORTA_NS}")

print(f"CPU: {monit.CPU()} %")
print(f"MEM: {monit.Memoria()} %")

# TODO: desenvolva mais duas opções de monitoramento da sua escolha
print(f"DISK: {monit.Disk()[3]} %")
print(f"NUMBER OF PIDS: {monit.Pids()}")
