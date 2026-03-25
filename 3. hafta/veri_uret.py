import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

satir = 500

degisken1 = np.random.normal(50, 10, satir)
degisken2 = np.random.normal(30, 5, satir)

df = pd.DataFrame({
    "Degisken1": degisken1,
    "Degisken2": degisken2
})

df.to_csv("veri.csv", index=False)

plt.scatter(df["Degisken1"], df["Degisken2"])
plt.title("Normal Dagilim")
plt.xlabel("Degisken1")
plt.ylabel("Degisken2")

plt.savefig("grafik.png")
plt.show()
