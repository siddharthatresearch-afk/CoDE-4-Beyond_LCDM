# CoDE-4 Compressed Observable χ² Analysis

## Overview

A preliminary compressed-observable chi-square (χ²) consistency analysis was performed to evaluate the phenomenological behavior of the CoDE-4 framework against key cosmological observables.

The statistical estimator used is:

χ² = Σ[(x_model − x_obs)² / σ²]

where:

- x_model = CoDE-4 prediction

- x_obs = observational value

- σ = observational uncertainty

This implementation currently serves as a preliminary consistency framework and does not yet include:

- covariance matrices,

- MCMC parameter estimation,

- Bayesian evidence comparison,

- or CLASS/CAMB perturbation pipelines.

---

# Included Observables

| Observable | Physical Sector |
|---|---|
| H₀ | Late-time expansion |
| R shift parameter | CMB geometry |
| l₁ acoustic peak | Recombination structure |
| S₈ | Weak-lensing clustering |
| z_eq | Matter-radiation equality |

---

# 1. Hubble Constant (H₀)

### Purpose

Tests late-time expansion consistency and the Hubble tension.

### Result

CoDE-4 reproduces the observed local expansion rate with extremely small χ² contribution.

### Interpretation

The framework successfully shifts the effective expansion history toward the locally inferred H₀ regime while preserving near-standard cosmological behavior.

---

# 2. CMB Shift Parameter (R)

### Purpose

Tests integrated geometric consistency between today and recombination.

### Result

The χ² contribution remains extremely small.

### Interpretation

CoDE-4 preserves large-scale CMB geometric consistency despite introducing late-time expansion modifications.

---

# 3. Acoustic Peak (l₁)

### Purpose

Tests the angular sound horizon at recombination.

### Result

The framework reproduces the acoustic peak structure with very small deviation.

### Interpretation

This supports the recursive acoustic stabilization structure of CoDE-4 and preserves near-standard recombination geometry.

---

# 4. Weak-Lensing S₈

### Purpose

Tests late-time matter clustering through weak gravitational lensing.

### Result

The dominant χ² contribution originates from the S₈ sector.

### Interpretation

CoDE-4 predicts somewhat enhanced late-time clustering relative to current weak-lensing observations.

This represents the primary residual tension in the current compressed-observable analysis.

---

# 5. Matter-Radiation Equality (z_eq)

### Purpose

Tests the transition epoch between radiation domination and matter domination.

### Result

The χ² contribution remains relatively small.

### Interpretation

The framework preserves near-standard equality timing and matter power-spectrum turnover behavior.

---

# Overall Interpretation

The compressed-observable analysis indicates:

- strong consistency with early-universe geometric observables,

- successful late-time expansion behavior,

- preserved acoustic structure,

- and near-standard equality evolution.

The dominant residual tension arises primarily from weak-lensing structure-growth diagnostics (S₈).

Overall, CoDE-4 behaves as a weakly dynamical late-time cosmological framework with near-ΛCDM early-universe recovery and perturbative late-time expansion deformation.

---

# Future Work

Planned future extensions include:

- covariance-aware likelihood analysis,

- Cobaya MCMC integration,

- CLASS/CAMB perturbation evolution,

- expanded BAO and supernova datasets,

- and Bayesian comparison against standard ΛCDM cosmology.
