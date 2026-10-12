import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  

df = pd.read_csv(r"C:\Users\UNAI\Desktop\matplot/precios_consolas.csv")
# Batazbestekoa
batazbestekoak = df[["Xbox", "PS5", "Switch", "PC"]].mean()
kontsolak = df[["Xbox", "PS5", "Switch"]]
plt.bar(batazbestekoak.index, batazbestekoak)
plt.title("Batazbesteko prezioa")
plt.ylabel("Prezioa (€)")
plt.xlabel("Kontsolak")

plt.show()
# 2  PC-a Kontsolak baino garestigoak 
pc_garestiago = (df["PC"] > kontsolak.max(axis=1)).sum()
besteak = len(df) - pc_garestiago


plt.bar(["PC garestiago", "Merkeagoak"], [pc_garestiago, besteak])


plt.title(" PC-a Kontsolak baino garestigoak ")
plt.ylabel("Egun kopurua")

plt.show()

# 3
merkeena = kontsolak.idxmin(axis=1).value_counts()
plt.figure()
plt.bar(merkeena.index, merkeena)
plt.title("Kontsola merkeena izan den egunak")
plt.ylabel("Egun kopurua")

plt.show()