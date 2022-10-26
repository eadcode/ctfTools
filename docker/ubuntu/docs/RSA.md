Formules

Cryptage avec la clé publique (N, e)
c = 𝑚^𝑒 mod N

Décryptage avec la clé secrète (p, q, d)
N = p × q
Φ(N) = (p-1)(q-1)
d = e^-1 mod Φ(N)
m = c^d mod N