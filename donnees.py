import os
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 5000
montant = np.round(rng.lognormal(6.2, 1.1, n), 2)
anciennete = rng.integers(0, 120, n)
freq = rng.poisson(3, n) + 1
nuit = rng.binomial(1, 0.15, n)
score = 2.2*(np.log10(montant)-3.0) - anciennete/60 + (freq-3)/3 + nuit*1.2
fraude = ((score + rng.normal(0, 0.35, n)) > 0.6).astype(int)

df = pd.DataFrame({'montant': montant, 'anciennete': anciennete,
                   'freq_24h': freq, 'nuit': nuit, 'fraude': fraude})
os.makedirs('data', exist_ok=True)
df.to_csv('data/transactions.csv', index=False)
print(f"data/transactions.csv ecrit : {len(df)} lignes, {df['fraude'].sum()} fraudes")