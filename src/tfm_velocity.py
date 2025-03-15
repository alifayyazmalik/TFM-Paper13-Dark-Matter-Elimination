import numpy as np

def tfm_velocity(r, M_vis, λ, β, G=4.3e-6):
    """
    Calculate TFM velocity profile (Eq. 6 from Paper #13).
    """
    v_newtonian = np.sqrt(G * M_vis / r)
    v_tfm_term = np.sqrt(λ * β**2 * (1 - np.exp(-2*r/β)))
    return np.sqrt(v_newtonian**2 + v_tfm_term**2)
