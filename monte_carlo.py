import numpy as np
from motion import simule_trajectoires


def prix_monte_carlo(
    s0: float,
    K: float,
    r: float,
    sigma: float,
    T: float,
    n_trajectoires: int,
    seed: int | None = None,
) -> tuple[float, float]:
    trajectoires = simule_trajectoires(
        s0, mu=r, sigma=sigma, T=T, n_pas=1, n_trajectoires=n_trajectoires, seed=seed
    )
    S_T = np.array([trajectoire[-1] for trajectoire in trajectoires])
    gains = np.maximum(S_T - K, 0)

    gains_actualises = np.exp(-r * T) * gains
    prix = gains_actualises.mean()
    erreur_type = gains_actualises.std(ddof=1) / np.sqrt(n_trajectoires)
    return prix, erreur_type


if __name__ == "__main__":
    # proche de 9.93, le prix de Black-Scholes
    prix, erreur_type = prix_monte_carlo(
        100, 100, 0.04, 0.2, 1, n_trajectoires=100000, seed=42
    )
    print(f"Prix Monte Carlo : {prix:.2f} (erreur type : {erreur_type:.2f})")
