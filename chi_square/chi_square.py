# ============================================================

# CoDE-4 CHI-SQUARE ENGINE

# chi_square.py

# ============================================================

import numpy as np

# ============================================================

# OBSERVATIONAL VALUES

# ============================================================

# Hubble Constant (SH0ES)

H0_obs = 73.04

sigma_H0 = 1.04

# CMB Shift Parameter

R_obs = 1.7502

sigma_R = 0.0046

# First Acoustic Peak

l1_obs = 220.6

sigma_l1 = 0.5

# Weak Lensing S8

S8_obs = 0.776

sigma_S8 = 0.017

# Matter-Radiation Equality

z_eq_obs = 3400

sigma_z_eq = 100

# ============================================================

# CoDE-4 MODEL VALUES

# ============================================================

H0_model = 72.86

R_model = 1.75002

l1_model = 220.72

S8_model = 0.8396

z_eq_model = 3499

# ============================================================

# CHI-SQUARE FUNCTION

# ============================================================

def chi2(model, obs, sigma):

    return ((model - obs) ** 2) / (sigma ** 2)

# ============================================================

# INDIVIDUAL CHI-SQUARES

# ============================================================

chi2_H0 = chi2(H0_model, H0_obs, sigma_H0)

chi2_R = chi2(R_model, R_obs, sigma_R)

chi2_l1 = chi2(l1_model, l1_obs, sigma_l1)

chi2_S8 = chi2(S8_model, S8_obs, sigma_S8)

chi2_eq = chi2(z_eq_model, z_eq_obs, sigma_z_eq)

# ============================================================

# TOTAL CHI-SQUARE

# ============================================================

chi2_total = (

    chi2_H0 +

    chi2_R +

    chi2_l1 +

    chi2_S8 +

    chi2_eq

)
