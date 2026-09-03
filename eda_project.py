import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

print(df.head())
print(df.shape)
print(df.info())

print(df.isnull().sum())


df['director'] = df['director'].fillna('Unknown')
print(df['director'].isnull().sum())


df['cast'] = df['cast'].fillna('Unknown')
print(df['cast'].isnull().sum())


df['country'] = df['country'].fillna('Unknown')
print(df['country'].isnull().sum())


df = df.dropna(subset=['date_added', 'rating', 'duration'])
print(df.isnull().sum())

print(df.duplicated().sum())


print(df.describe())



print(df['type'].value_counts())



print(df['rating'].value_counts().head(5))



df['rating'].value_counts().head(5).plot(kind='bar')
plt.title('Top 5 Ratings of Movies and TV Shows on Netflix')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.savefig('charts/top5_ratings.png')
plt.show()