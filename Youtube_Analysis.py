# YouTube Data Analysis & Visualization
# Author: Faiq
# Description: Exploratory Data Analysis on YouTube trending videos dataset.

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_style("whitegrid")

# Load dataset (replace with your actual file name if needed)
df = pd.read_csv("youtube_dataset.csv", low_memory=False)

# --- Basic info ---
print("Dataset shape:", df.shape)
print("\nColumn names:\n", df.columns)
print("\nMissing values:\n", df.isnull().sum().sort_values(ascending=False).head(10))

# --- Clean column names ---
df.columns = df.columns.str.lower().str.strip()

# --- Check key columns ---
key_cols = ['title', 'views', 'likes', 'dislikes', 'comment_count', 'categoryid', 'channeltitle']
for col in key_cols:
    if col not in df.columns:
        print(f"⚠️ Missing column: {col}")

# --- Handle missing data ---
df = df.dropna(subset=['views', 'likes', 'comment_count'])

# --- Convert numeric columns ---
num_cols = ['views', 'likes', 'dislikes', 'comment_count']
for col in num_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# --- Visualization 1: Most common categories ---
if 'categoryid' in df.columns:
    plt.figure(figsize=(8,4))
    sns.countplot(x='categoryid', data=df, order=df['categoryid'].value_counts().index)
    plt.title("Most Common Video Categories")
    plt.xlabel("Category ID")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# --- Visualization 2: Top 10 Most Viewed Videos ---
if 'views' in df.columns:
    top_videos = df.sort_values(by='views', ascending=False).head(10)
    plt.figure(figsize=(10,5))
    sns.barplot(y='title', x='views', data=top_videos, palette='viridis')
    plt.title("Top 10 Most Viewed YouTube Videos")
    plt.xlabel("Views")
    plt.ylabel("Video Title")
    plt.tight_layout()
    plt.show()

# --- Visualization 3: Relationship between Views, Likes, and Comments ---
plt.figure(figsize=(7,5))
sns.scatterplot(x='likes', y='views', data=df, alpha=0.5)
plt.title("Views vs Likes")
plt.xlabel("Likes")
plt.ylabel("Views")
plt.tight_layout()
plt.show()

# --- Visualization 4: Correlation Heatmap ---
corr = df[num_cols].corr()
plt.figure(figsize=(6,5))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Between Key Metrics")
plt.tight_layout()
plt.show()

# --- Visualization 5: Top Channels by Trending Videos ---
if 'channeltitle' in df.columns:
    top_channels = df['channeltitle'].value_counts().head(10)
    plt.figure(figsize=(9,5))
    sns.barplot(x=top_channels.values, y=top_channels.index, palette='mako')
    plt.title("Top 10 Channels by Trending Videos")
    plt.xlabel("Number of Trending Videos")
    plt.ylabel("Channel Name")
    plt.tight_layout()
    plt.show()

print("\n✅ Analysis completed successfully!")
