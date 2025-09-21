import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

# Load data
df = pd.read_csv('metadata.csv', low_memory=False)
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract_word_count'] = df['abstract'].fillna('').apply(lambda x: len(x.split()))
df['journal'] = df['journal'].fillna('Unknown')

# Clean data
missing_ratio = df.isnull().mean()
high_missing = missing_ratio[missing_ratio > 0.5]
df_cleaned = df.drop(columns=high_missing.index)
df_cleaned = df_cleaned.dropna(subset=['title', 'publish_time'])

# Streamlit layout
st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers from the CORD-19 dataset")

# Year filter
year_range = st.slider("Select publication year range", 2019, 2022, (2020, 2021))
filtered_df = df_cleaned[(df_cleaned['year'] >= year_range[0]) & (df_cleaned['year'] <= year_range[1])]

# Show sample data
st.subheader("Sample Data")
st.dataframe(filtered_df[['title', 'journal', 'year']].head(10))

# Publications by year
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax1, palette='Blues')
ax1.set_title('Number of Publications by Year')
st.pyplot(fig1)

# Top journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax2, palette='Greens')
ax2.set_title('Top 10 Journals')
st.pyplot(fig2)

# Common words in titles
st.subheader("Common Words in Titles")
titles = filtered_df['title'].dropna().str.lower().str.cat(sep=' ')
words = re.findall(r'\b[a-z]{4,}\b', titles)
common_words = Counter(words).most_common(15)
words, counts = zip(*common_words)
fig3, ax3 = plt.subplots()
sns.barplot(x=list(words), y=list(counts), ax=ax3, palette='Purples')
ax3.set_title('Most Common Words in Titles')
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45)
st.pyplot(fig3)
