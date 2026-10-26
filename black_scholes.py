import numpy as np
from scipy.stats import norm


def prix_black_scholes(s0: float, K: float, r: float, sigma: float, T: float) -> float:
    d1 = (np.log(s0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return s0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


if __name__ == "__main__":
    prix = prix_black_scholes(100, 100, 0.04, 0.2, 1)
    print(f"Prix Black-Scholes : {prix:.2f}")  # doit donner 9.93
