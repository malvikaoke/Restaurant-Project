import pandas as pd
df= pd.read_csv(r'C:\Users\okeud\PycharmProjects\Future50_rankings.csv.csv')
print(df)
print(df.head(50))
print(df.columns)
print(df.isnull().sum())
print(df['Location'])
print(df[df["Location"] =="New York, N.Y."])
print(df[(df["Location"]== "New York, N.Y.") & (df["Franchising"]== "Yes")])
print(df[(df["Location"]== "New York, N.Y.") & (df["Franchising"]== "No")])
print(df[df["Location"] =="New York, N.Y."].groupby(["Franchising"]).agg({"Sales":"sum"}))

df= pd.read_csv(r'C:\Users\okeud\PycharmProjects\Independence100_ranking.csv.csv')
print(df)
df.shape
df.info()
print(df[df["City"] =="New York"])
print(df[df["City"] =="New York"].agg({"Sales":"sum"}))
print(df.sort_values(by=['State', 'Meals Served']))
print(df.sort_values(by=['State', 'Meals Served'], ascending=False))
print(df.sort_values(by=['Rank', 'State']))
drop_dup = df.drop_duplicates(subset=['Average Check'])
print(df.head(10))
print(df.loc[1:10,"Rank":"Meals Served"])
print(df.iloc[0:5,1:5])

df= pd.read_csv(r'C:\Users\okeud\PycharmProjects\Top250_rankings.csv.csv')
print(df)
print(df.loc[1:10,"Restaurant":"Segment_Category"])
print(df.head(5))
print(df[df['Segment_Category']=="Quick Service & Burger"]["Restaurant"])
print(df.describe())
print(df.head())
print(df.iloc(0))
print(df.sort_values(by=['Sales']))
print(df.head(15))







