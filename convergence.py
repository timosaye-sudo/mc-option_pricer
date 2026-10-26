import matplotlib.pyplot as plt
import numpy as np
from black_scholes import prix_black_scholes
from monte_carlo import prix_monte_carlo

s0, K, r, sigma, T = 100, 100, 0.04, 0.2, 1
prix_bs = prix_black_scholes(s0, K, r, sigma, T)

liste_n = np.logspace(2, 5, 20).astype(int)
liste_prix, liste_erreurs = [], []

for n in liste_n:
    prix, erreur = prix_monte_carlo(s0, K, r, sigma, T, n_trajectoires=n, seed=42)
    liste_prix.append(prix)
    liste_erreurs.append(erreur)

plt.figure(figsize=(8, 5))
plt.errorbar(
    liste_n,
    liste_prix,
    yerr=liste_erreurs,
    fmt="o-",
    capsize=3,
    label="Prix Monte Carlo avec erreur type",
)
plt.axhline(prix_bs, color="red", linestyle="--", label="Prix Black-Scholes")
plt.xscale("log")
plt.xlabel("Nombre de simulations")
plt.ylabel("Prix de l'option")
plt.legend()
plt.title("Convergence du prix Monte Carlo vers Black-Scholes")
plt.savefig("convergence.png")
plt.show()
