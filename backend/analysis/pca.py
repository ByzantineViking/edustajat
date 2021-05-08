from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

valitut_path = Path('manual_data/kuntavaalit2017/restructured/valitut.csv')

valitut = pd.read_csv(valitut_path)


valitut_features = valitut[[
    'ennakkoäänet',
    'vaalipäivän_äänet',
]]


pca = PCA(n_components=2)

principalComponents = pca.fit_transform(valitut_features)
principalDf = pd.DataFrame(data=principalComponents, columns=[
                           'principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, valitut], axis=1)


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 component PCA', fontsize=20)
targets = [1, 2]
colors = ['r', 'b']
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['sukupuoli'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
               finalDf.loc[indicesToKeep, 'principal component 2'], c=color, s=50)
ax.legend(targets)
ax.grid()


fig.show()
fig.savefig("sukupuoli_äänet.png")
