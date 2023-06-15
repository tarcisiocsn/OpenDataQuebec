import pandas as pd
data = pd.read_csv('./comptage-feux-2014-2018.csv')
tmp = data[(data.Date > '2018-01-01') & (data.Description_Code_Banque == 'Autos')]
#tmp[['Id_Intersection', 'Heure']].groupby(['Id_Intersection']).count()
#x = tmp[['Id_Intersection', 'Heure']].groupby(['Id_Intersection']).count()
#x.sort_values(by = 'Heure')
i1249 = tmp[tmp.Id_Intersection == 1249]
for t in i1249.Date.unique():
    x = i1249[i1249.Date == t]
    plot(x.Heure+x.Minute/60., x.NBT)

# TODO sum the different movements
