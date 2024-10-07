import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy 

# Définir les chemins des fichiers
hust = '../data/HUST data'
mit1 = '../data/MIT data/2017-05-12'
mit2 = '../data/MIT data/2017-06-30'
mit3 = '../data/MIT data/2018-04-12'
tju1 = '../data/TJU data/Dataset_1_NCA_battery'
tju2 = '../data/TJU data/Dataset_2_NCM_battery'
tju3 = '../data/TJU data/Dataset_3_NCM_NCA_battery'
xjtu = '../data/XJTU data'

roots = [hust, mit1, mit2, mit3, tju1, tju2, tju3, xjtu]

total_numbers = 0
battery_numbers = 0

for root in roots[:4:]:
    sub_total = 0
    files = os.listdir(root)
    num = len(files)
    
    for i, f in enumerate(files[-1:]):
        df = pd.read_csv(os.path.join(root, f))
        print(df)

        # Tracer la moyenne de la tension
        ax = df.plot(y='voltage mean', marker='o', figsize=(8, 5), title=f'Voltage Mean from {f}')
        ax.set_xlabel('Index')
        ax.set_ylabel('Voltage Mean')
        plt.grid()

        plt.savefig('my_plot.png')  # Enregistre le graphique sous forme d'image PNG
        nums = df.shape[0]
        sub_total += nums

    print(f'data set {root} has {num} files, {sub_total} samples !')
    print(df.columns)
    total_numbers += sub_total
    battery_numbers += num

print('total samples:', total_numbers)
print('total batteries:', battery_numbers)
plt.show(block=True)  # S'assurer que le plot s'affiche
