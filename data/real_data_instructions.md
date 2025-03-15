# How to Use Real Data

1. Format your data as CSV with 3 columns:
r (kpc), v_obs (km/s), err_v (km/s)
2. Overwrite `data/ngc3198.csv` with your data
3. Run the code:
```bash
python src/chi2_fitter.py
