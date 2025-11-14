import random

n = 100000
prob = sum(random.choice(["cara", "cruz"]) == "cara" for _ in range(n)) / n

print("Probabilidad de obtener cara:", prob)