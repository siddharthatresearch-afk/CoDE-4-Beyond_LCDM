# CoDE-4 Derivations Overview

## Overview

This document summarizes the current mathematical, phenomenological, perturbative, asymptotic, and numerical derivation sectors developed within the CoDE-4 cosmological framework.

The purpose of this overview is to provide:
- a unified map of all current derivation sectors,
- a summary of the implemented mathematical structure,
- and an overview of the numerical and observational consistency results obtained within the current framework.

The present CoDE-4 implementation should be interpreted as:
- a phenomenological modified-expansion cosmology framework,
- with bounded late-time vacuum deformation,
- numerical perturbation evolution,
- compressed-observable reconstruction,
- and asymptotic recovery of near-standard early-universe cosmology.

The framework remains exploratory and under active development.

---

# 1. Modified Expansion Framework

The core CoDE-4 expansion structure modifies the effective vacuum sector through the bounded deformation function:

$$
C(z) = 1 + \epsilon \left( \frac{z}{(1+z)^2} \right) \left( 1 - \frac{0.15}{1+z} \right)
$$

which enters the modified expansion equation:

$$
H^2(z) = H_0^2 \left[ \Omega_m(1+z)^3 + \Omega_r(1+z)^4 + \Omega_\Lambda C(z) \right]
$$

The deformation was intentionally constructed to:
- remain bounded,
- preserve high-redshift recovery,
- produce weak late-time expansion modification,
- and maintain near-standard early-universe behavior.

---

# 2. Asymptotic Recovery Structure

One of the central properties of the framework is asymptotic recovery of standard cosmological evolution.

At sufficiently high redshift:

$$
z \to \infty
$$

the framework satisfies:

$$
C(z) \to 1
$$

This produces:
- preserved radiation domination,
- stable recombination-era evolution,
- bounded perturbation behavior,
- and near-standard early-universe cosmology.

Current numerical evolution demonstrates:
- approximately zero-percent BBN deviation,
- stable damping-tail evolution,
- and preserved recombination consistency.

---

# 3. Effective Dark-Energy Reconstruction

The modified vacuum sector may be interpreted phenomenologically as an evolving effective dark-energy component through:

$$
\rho_X(z) = \rho_\Lambda C(z)
$$

leading to an effective equation-of-state evolution:

$$
w_{\mathrm{eff}}(z) = -1 + \frac{1+z}{3C(z)} \frac{dC}{dz}
$$

The resulting behavior remains:
- weakly dynamical,
- near-$\Lambda$CDM,
- and perturbatively bounded.

Current effective evolution produces approximately:
- $w_0 \approx -0.986$
- $w_a \approx -0.052$

within a CPL-style interpretation.

---

# 4. Taylor and Perturbative Expansion Analysis

The framework admits a perturbative low-redshift expansion through Taylor-series analysis of the deformation sector.

The resulting expansion demonstrates:
- bounded low-redshift corrections,
- smooth perturbative evolution,
- finite asymptotic behavior,
- and controlled late-time modification.

This perturbative structure forms one of the mathematical stability foundations of the framework.

---

# 5. Acoustic Reconstruction

The CoDE-4 numerical engine reconstructs:
- the sound horizon,
- angular acoustic scale,
- recombination-distance geometry,
- and first acoustic peak structure.

The sound horizon is computed numerically through:

$$
r_s(z) = \int_z^\infty \frac{c_s(z')}{H(z')} \, dz'
$$

Current numerical reconstruction produces:
- Acoustic scale:
  - $l_A \approx 302.36$
- First acoustic peak:
  - $l_1 \approx 220.72$

which remains extremely close to standard observational constraints.

This indicates preservation of:
- recombination-era plasma dynamics,
- sound-horizon evolution,
- and acoustic consistency.

---

# 6. Shift-Parameter Reconstruction

The framework additionally reconstructs the CMB shift parameter:

$$
R = \frac{\sqrt{\Omega_m} H_0}{c} D_M(z_*)
$$

through numerical integration of the modified expansion history.

Current numerical reconstruction produces:

$$
R \approx 1.75002
$$

which remains strongly consistent with standard observational constraints.

This indicates preservation of:
- integrated expansion geometry,
- recombination-distance structure,
- and large-scale cosmological geometry.

---

# 7. Perturbation Growth Evolution

The CoDE-4 engine numerically evolves linear matter perturbations through the modified background expansion history.

The perturbation sector is evolved with respect to scale factor $a$ (where $' \equiv d/da$) through:

$$
\delta'' + \left( \frac{3}{a} + \frac{H'}{H} \right)\delta' - \frac{3 H_0^2 \Omega_m}{2 a^5 H^2}\delta = 0
$$

using finite-step numerical integration across cosmological scale-factor evolution.

The resulting perturbation evolution remains:
- finite,
- smooth,
- bounded,
- and numerically stable.

The framework currently reconstructs:
- $f\sigma_8(z)$ evolution,
- growth-index behavior,
- ISW potential decay,
- and weak-lensing observables.

---

# 8. ISW and Potential Evolution

The Integrated Sachs-Wolfe sector is evaluated numerically through normalized sub-horizon gravitational potential evolution:

$$
\Phi(a) = \frac{\delta(a)}{a}
$$

Current numerical evolution demonstrates:
- stable potential decay,
- negative $d\Phi/d\ln(a)$ behavior,
- and standard dark-energy-dominated ISW evolution.

This indicates stable late-time perturbative evolution within the current framework.

---

# 9. Equality and Turnover Consistency

The framework additionally preserves near-standard matter-radiation equality evolution.

Current numerical reconstruction produces:

$$
z_{eq} \approx 3499
$$

which remains within the expected standard cosmological range.

The framework additionally reconstructs:
- matter power-spectrum turnover scales,
- equality-era expansion behavior,
- and early structure-formation consistency.

---

# 10. Structure-Growth and Weak-Lensing Sector

The current framework numerically reconstructs:
- $\sigma_8$ evolution,
- $S_8$ behavior,
- and structure-growth diagnostics.

Current numerical reconstruction produces approximately:
- $\sigma_8 \approx 0.8194$
- $S_8 \approx 0.8396$

The dominant residual phenomenological tension within the framework currently arises in:
- weak-lensing clustering amplitudes,
- and matter power-spectrum turnover behavior.

However, these tensions currently represent:
- observational consistency limitations,
rather than:
- mathematical or dynamical instabilities.

---

# 11. Hubble Tension Reconstruction

One of the primary phenomenological motivations of the framework is modification of late-time expansion behavior while preserving early-universe consistency.

The current CoDE-4 numerical reconstruction produces:

$$
H_0 \approx 72.86 \ \mathrm{km/s/Mpc}
$$

which remains close to local-distance-ladder measurements.

The resulting reconstructed tension relative to local SH0ES measurements is currently:

$$
\approx 0.17\sigma
$$

compared to approximately:

$$
\approx 4.89\sigma
$$

within standard Planck $\Lambda$CDM reconstruction.

---

# 12. Stability Properties

The framework currently demonstrates:
- bounded deformation behavior,
- asymptotic recovery of standard cosmology,
- stable perturbation evolution,
- preserved recombination structure,
- stable acoustic geometry,
- and numerically stable background evolution.

The framework does not currently exhibit:
- divergent perturbations,
- runaway expansion,
- asymptotic singularities,
- or unstable ISW behavior.

---

# Current Interpretation

The present CoDE-4 framework currently behaves as:
- a phenomenological modified-expansion cosmology framework,
- with bounded late-time vacuum deformation,
- numerical perturbation evolution,
- preserved early-universe recovery,
- and preliminary compressed-observable consistency.

The framework remains:
- exploratory,
- phenomenological,
- and under active development.

Future planned extensions include:
- covariance-aware likelihood analysis,
- Cobaya integration,
- CLASS/CAMB compatibility,
- full MCMC parameter estimation,
- and expanded observational dataset integration.
