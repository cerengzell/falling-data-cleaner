import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
df = pd.read_csv('data.csv')

plt.figure(figsize=(8,6))
plt.scatter(df['Degisken_1'], df['Degisken_2'], color='purple', alpha=0.6)
plt.title('İki Değişkenli Normal Dağılımlı Veri')
plt.xlabel('Degisken_1 (birim1)')
plt.ylabel('Degisken_2 (birim2)')
plt.grid(True)
plt.savefig('grafikler.png')
plt.show()
