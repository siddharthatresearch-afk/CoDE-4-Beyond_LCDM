# Equality and Turnover Reconstruction

## Overview

One of the most important early-universe consistency diagnostics in cosmology is preservation of the matter-radiation equality epoch and the associated matter power-spectrum turnover scale.

These sectors directly influence:
- early structure formation,
- perturbation growth,
- matter power-spectrum geometry,
- and large-scale clustering evolution.

Because the CoDE-4 framework modifies the cosmological expansion sector through a bounded perturbative deformation, reconstruction of the equality epoch and the turnover scale provides an important test of early-universe consistency and perturbative stability.

The purpose of this derivation is therefore to:
- reconstruct the matter-radiation equality epoch,
- derive the turnover-scale behavior,
- analyze perturbative consistency,
- and connect the framework directly to large-scale structure observables.

---

# Matter-Radiation Equality

Matter-radiation equality occurs when the physical energy density of matter balances the total relativistic radiation energy density:

$$
\rho_m(a) = \rho_r(a)
$$

Using standard cosmological scaling relations, $\rho_m(a) \propto a^{-3}$ and $\rho_r(a) \propto a^{-4}$, the equality condition becomes:

$$
\Omega_m(1+z_{eq})^3 = \Omega_r(1+z_{eq})^4
$$

Dividing both sides by $(1+z_{eq})^3$ yields:

$$
1+z_{eq} = \frac{\Omega_m}{\Omega_r}
$$

Therefore, the exact mathematical boundary for the redshift of equality reduces to:

$$
z_{eq} = \frac{\Omega_m}{\Omega_r} - 1
$$

where:
- $\Omega_m$ represents the total matter density parameter today,
- and $\Omega_r$ represents the total radiation density parameter today (including photons and relativistic neutrinos).

---

# Numerical Equality Reconstruction

Using the current CoDE-4 numerical engine configuration parameters ($\Omega_m \approx 0.315$ and $\Omega_r \approx 9 \times 10^{-5}$), the framework reconstructs:

$$
z_{eq} \approx 3499
$$

This remains consistent with standard cosmological expectations and Planck-era equality constraints. The framework therefore preserves near-standard equality timing, stable early-universe expansion, and bounded perturbative evolution.

---

# Physical Importance of Equality

The equality epoch acts as a critical transition in cosmological evolution.

Before equality:
- radiation dominates expansion dynamics,
- perturbation growth becomes strongly suppressed,
- and relativistic effects dominate cosmological evolution.

After equality:
- matter domination begins,
- gravitational instability becomes efficient,
- and large-scale structure formation accelerates.

Small changes to the equality epoch or the expansion rate near equality can therefore significantly alter matter power spectra, clustering geometry, and structure-growth evolution.

---

# Modified Expansion Background

The CoDE-4 framework modifies the cosmological background through the exact operational relation:

$$
H^2(z) = H_0^2 \left[ \Omega_m(1+z)^3 + \Omega_r(1+z)^4 \left( 1+\frac{\epsilon z}{(1+z)^3} \right) + \Omega_\Lambda C(z) \right]
$$

where the active deformation profile is defined as:

$$
C(z) = 1 + \epsilon \left( \frac{z}{(1+z)^2} \right) \left( 1 - \frac{0.15}{1+z} \right)
$$

Because the deformation becomes asymptotically suppressed and the radiation correction vanishes rapidly at high redshift, the equality sector remains close to standard cosmological behavior.

---

# Asymptotic Equality Recovery

At sufficiently large redshift, the deformation dynamics freeze out cleanly:

$$
\frac{\epsilon z}{(1+z)^3} \to 0 \quad \text{and} \quad C(z) \to 1
$$

Therefore, the modified expansion framework asymptotically approaches standard cosmological evolution, preserving radiation domination and stable equality behavior. This asymptotic recovery is one of the primary stability properties of the framework.

---

# Matter Power-Spectrum Turnover

The equality epoch determines the characteristic turnover scale of the matter power spectrum. The turnover scale is reconstructed through:

$$
k_{eq} = \frac{a_{eq} H(z_{eq})}{c}
$$

where:
- $a_{eq}$ is the equality scale factor,
- and $H(z_{eq})$ is the expansion rate at equality.

The equality scale factor satisfies:

$$
a_{eq} = \frac{1}{1+z_{eq}}
$$

The turnover scale therefore depends directly on equality timing, expansion evolution, and radiation-era dynamics.

---

# Numerical Turnover Reconstruction

The current CoDE-4 numerical engine reconstructs approximately:

$$
k_{eq} \approx 0.01566\ h/\mathrm{Mpc}
$$

while the standard theoretical expectation is approximately:

$$
k_{eq}^{\mathrm{std}} \approx 0.01675\ h/\mathrm{Mpc}
$$

The resulting deviation is approximately $6.5\%$. This represents one of the primary residual phenomenological deviations within the current framework. However, the turnover evolution remains finite, bounded, and numerically stable.

---

# Structure-Growth Connection

The turnover scale connects directly to matter clustering, perturbation growth, weak-lensing evolution, and large-scale structure formation. Because the framework preserves near-standard equality timing, stable perturbation evolution, and bounded expansion behavior, the resulting matter power-spectrum evolution remains phenomenologically reasonable and perturbatively stable.

---

# Stability Interpretation

The equality and turnover sectors act as important early-universe stability diagnostics and perturbative consistency tests. Current numerical reconstruction demonstrates preserved equality timing, stable radiation-era evolution, and bounded large-scale clustering behavior. The framework therefore avoids catastrophic equality shifts, unstable radiation domination, and divergent turnover evolution.

---

# Phenomenological Interpretation

Overall, the CoDE-4 framework reconstructs stable matter-radiation equality evolution, bounded turnover-scale behavior, near-standard early-universe expansion, and perturbatively stable structure formation. The framework therefore currently behaves as a phenomenologically stable modified-expansion cosmology framework, with weak late-time deformation, while preserving near-standard equality-era cosmological evolution.
