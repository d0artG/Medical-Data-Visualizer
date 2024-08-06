import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = df["weight"]/((df["height"]*0.01)**2)
df["overweight"] = np.where(df["overweight"]>25, 1,0)

# 3
df[["cholesterol","gluc"]]=np.where(df[["cholesterol", "gluc"]]==1,0,1)

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars="cardio",value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # 6
    df_cat = df_cat.value_counts().reset_index()
    df_cat.rename(columns={"count": "total"}, inplace=True)
    df_cat2 = df_cat.sort_values(["variable","cardio","value"])

    # 7



    # 8
    fig = sns.catplot(data=df_cat2,x="variable",y="total",kind="bar", hue="value", col="cardio")


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.copy()
    df_heat.drop(df_heat[(df['ap_lo'] > df_heat['ap_hi'])].index, inplace=True)
    df_heat.drop(df_heat[(df_heat['height'] < df_heat['height'].quantile(0.025)) | (df_heat['height']> df_heat['height'].quantile(0.975))].index, inplace = True)
    df_heat.drop(df_heat[(df_heat['weight'] < df_heat['weight'].quantile(0.025)) | (df_heat['weight']> df_heat['weight'].quantile(0.975))].index, inplace = True)

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr))



    # 14
    fig,ax=plt.subplots()

    # 15
    sns.heatmap(data=corr, mask=mask, annot=True,fmt='.1f', ax=ax)


    # 16
    fig.savefig('heatmap.png')
    return fig
