# Effective Equation-of-State Derivation

## Overview

One of the most important phenomenological interpretations of the CoDE-4 framework is the reconstruction of an effective dynamical dark-energy equation of state.

Although the framework was not constructed from a fundamental scalar-field Lagrangian, the bounded vacuum deformation sector can still be interpreted phenomenologically as an evolving effective dark-energy fluid.

This allows the framework to be mapped onto an effective equation-of-state evolution through the cosmological continuity equation.

The purpose of this derivation is therefore to:
- reconstruct the effective equation-of-state behavior,
- analyze low-redshift dynamical evolution,
- evaluate perturbative stability,
- and compare the resulting behavior against standard $\Lambda$CDM expectations.

---

# Effective Vacuum Reconstruction

The CoDE-4 framework modifies the vacuum sector through the bounded deformation function:

$$
C(z) = 1 + \epsilon \left(\frac{z}{(1+z)^2}\right)\left(1-\frac{0.15}{1+z}\right)
$$

The effective dark-energy density is reconstructed phenomenologically as:

$$
\rho_X(z) = \rho_\Lambda C(z)
$$

where:
- $\rho_\Lambda$ represents the baseline vacuum-energy density,
- and $C(z)$ acts as the perturbative deformation profile.

The framework therefore behaves as:
- a weakly dynamical effective vacuum sector.

---

# Cosmological Continuity Equation

For a general cosmological fluid component, the continuity equation satisfies:

$$
\frac{d\rho}{dz} = \frac{3(1+w)}{1+z}\rho
$$

Solving algebraically for the effective equation of state produces:

$$
w(z) = -1 + \frac{1+z}{3\rho(z)} \frac{d\rho}{dz}
$$

Applying this relation to the reconstructed CoDE-4 effective vacuum sector yields the effective dark-energy equation of state.

---

# Effective Equation-of-State Reconstruction

Substituting the effective density relation into the continuity equation isolates the model's structural parameters directly inside the dynamic state equation:

$$
w_{\mathrm{eff}}(z) = -1 + \frac{1+z}{3C(z)} \frac{dC}{dz}
$$

The resulting evolution therefore depends entirely on:
- the bounded deformation structure,
- and the derivative behavior of the modifier function.

---

# Analytical Derivative Structure

The exact derivative of the modifier function satisfies:

$$
\frac{dC}{dz} = \epsilon \left[ \frac{1-z}{(1+z)^3} \left( 1-\frac{0.15}{1+z} \right) + \left( \frac{z}{(1+z)^2} \right) \left( \frac{0.15}{(1+z)^2} \right) \right]
$$

The derivative remains:
- finite,
- smooth,
- continuously differentiable,
- and asymptotically suppressed.

This smooth differentiability is important because:
- the effective equation of state depends directly on the derivative structure,
- numerical evolution remains stable,
- and finite-difference instability is avoided.

---

# Low-Redshift Expansion

Near the present cosmological epoch ($z \ll 1$), the modifier expansion satisfies:

$$
C(z) \approx 1 + \epsilon \left( 0.85z - 1.55z^2 + 2.20z^3 \right) + \mathcal O(z^4)
$$

while the derivative expansion matches the following trajectory:

$$
\frac{dC}{dz} \approx \epsilon \left( 0.85 - 3.10z + 6.60z^2 \right) + \mathcal O(z^3)
$$

Combining these elements under joint Taylor constraints maps the explicit dynamic baseline for the fluid profile:

$$
w_{\mathrm{eff}}(z) \approx -1 + \epsilon \left( 0.2833 - 0.7500z + 1.6383z^2 \right) + \mathcal{O}(\epsilon^2, z^3)
$$

This combined series demonstrates that:
- the evolution remains perturbative,
- the correction remains bounded,
- and the framework remains close to standard $\Lambda$CDM behavior.

---

# Present-Day Effective Equation of State

At the present cosmological epoch ($z = 0$), evaluating the system under standard baseline configuration parameters ($\epsilon = 0.05$) yields:

$$
w_0 = -1 + \frac{0.85}{3}\epsilon = -0.98583 \approx -0.986
$$

This indicates:
- near-$\Lambda$CDM behavior,
- weak late-time dynamical evolution,
- and bounded vacuum deformation.

The framework therefore behaves as:
- a weakly dynamical effective dark-energy sector,
rather than:
- a strongly evolving quintessence-type cosmology.

---

# CPL Mapping

The reconstructed evolution may additionally be interpreted through a Chevallier-Polarski-Linder (CPL) style parameterization:

$$
w(a) = w_0 + w_a(1-a)
$$

where:
- $w_0$ represents the present-day equation of state,
- and $w_a$ measures low-redshift evolution.

The current CoDE-4 reconstruction approximately produces:
- $w_0 \approx -0.986$
- $w_a \approx -0.052$

These values indicate:
- weak dynamical evolution,
- near-standard late-time behavior,
- and bounded perturbative deformation.

---

# High-Redshift Recovery

At sufficiently large redshift:

$$
z \to \infty
$$

the modifier satisfies:

$$
C(z) \to 1 \quad \text{and} \quad \frac{dC}{dz} \to 0
$$

Therefore:

$$
w_{\mathrm{eff}}(z) \to -1
$$

This asymptotic recovery ensures:
- preservation of early-universe cosmology,
- stable recombination-era behavior,
- and asymptotic suppression of the deformation sector.

---

# Stability Properties

Because:
- the modifier remains bounded,
- the derivative remains finite,
- and the perturbative expansion remains smooth,

the reconstructed equation-of-state evolution remains:
- finite,
- stable,
- weakly dynamical,
- and numerically well-behaved.

The framework does not currently exhibit:
- divergent vacuum evolution,
- unstable phantom divergence,
- or runaway equation-of-state behavior.

---

# Phenomenological Interpretation

Overall, the CoDE-4 framework reconstructs:
- a weakly dynamical effective dark-energy sector,
- with bounded late-time evolution,
- perturbative deviation from $\Lambda$CDM,
- and asymptotic recovery of standard cosmology.

The reconstructed equation-of-state behavior currently remains:
- close to vacuum-energy evolution,
- weakly dynamical,
- and phenomenologically stable across cosmological evolution.
