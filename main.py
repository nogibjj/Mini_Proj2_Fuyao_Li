import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Specify the file path and the sheet name
file_path = 'Durham-Observatory-monthly-mean-temperature.xlsx'
sheet_name = 'Durham monthly Tmean'

# Read the specific sheet into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Calculate the average of every month
mean_values = df.iloc[:, 1:13].mean()

# Calculate mean, median, and standard deviation
mean_temp = df.iloc[:, 1:13].mean()
median_temp = df.iloc[:, 1:13].median()
std_temp = df.iloc[:, 1:13].std()

stats_df = pd.DataFrame({
    "Mean": mean_temp,
    "Median": median_temp,
    "Standard deviation": std_temp
}).T

# Calculate mean, median, and standard deviation
print(f'The mean of the temperature from 1795 to 2021 is {mean_temp}')
print(f'The median of the temperature from 1795 to 2021 is {median_temp}')
print(f'The standard deviation of the temperature from 1795 to 2021 is {std_temp}')


# 1. Line Plot of Monthly Average Temperature Over Time
plt.figure(figsize=(12, 6))
plt.plot(df.iloc[:-1, 0], df.iloc[:-1, 1:13].mean(axis=1), label='Mean Temperature', color='royalblue')
plt.title('Mean Temperature (1795-2021)')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.savefig('average.png', dpi=300)
plt.show()

# 2. Heatmap of Monthly Temperatures Over the Years
plt.figure(figsize=(10, 20))
sns.heatmap(df.iloc[:-1, 1:13], cmap='coolwarm', cbar_kws={'label': 'Temperature (°C)'}, yticklabels=df.iloc[:-1, 0])
plt.title('Monthly Temperatures (1795-2021)')
plt.xlabel('Month')
plt.ylabel('Year')
plt.savefig('heatmap.png', dpi=300)
plt.show()

# Writing results and figures to Markdown file
with open('temperature_analysis.md', 'w') as f:
    # Write the title
    f.write("# Temperature Analysis (1795-2021)\n\n")

    # Write the summary statistics as tables
    f.write("## Summary Statistics\n")

    header = "| T (&deg;C)         | " + " | ".join(stats_df.columns) + " |\n"
    separator = "| ------------------ |" + " ---- |" * len(stats_df.columns) + "\n"
    
    rows = ""
    for index, row in stats_df.iterrows():
        row_str = f"| {index:<18} | " + " | ".join([f"{value:.2f}" for value in row]) + " |\n"
        rows += row_str
    
    markdown_table = header + separator + rows
    f.write(markdown_table)

    # Insert the line plot image
    f.write("## Mean Temperature Over Time (1795-2021)\n")
    f.write("![Mean Temperature](average.png)\n\n")

    # Insert the heatmap image
    f.write("## Monthly Temperature Heatmap (1795-2021)\n")
    f.write("![Heatmap](heatmap.png)\n")

