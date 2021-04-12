import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight']/(df['height']/100)**2

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['overweight'] = df['overweight'].apply(lambda x: 0 if x<=25 else 1)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
	# Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
	df_cat = pd.melt(df, id_vars='cardio', value_vars=['alco', 'active','cholesterol', 'gluc', 'smoke', 'overweight'])
	# Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.

	# Draw the catplot with 'sns.catplot()'
	fig = sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio')

	# Do not modify the next two lines
	fig.savefig('catplot.png')
	return fig


# Draw Heat Map
def draw_heat_map():
	# Clean the data
	df_heat = df
	df_heat = df_heat.loc[(df_heat['ap_lo'] <= df_heat['ap_hi'])]
	df_heat = df_heat.loc[(df_heat['height'] >= df_heat['height'].quantile(0.025))]
	df_heat = df_heat.loc[(df_heat['height'] <= df_heat['height'].quantile(0.975))]
	df_heat = df_heat.loc[(df_heat['weight'] >= df_heat['weight'].quantile(0.025))]
	df_heat = df_heat.loc[(df_heat['weight'] <= df_heat['weight'].quantile(0.975))]

	# Calculate the correlation matrix
	corr = df_heat.corr()

	# Generate a mask for the upper triangle
	mask = np.zeros_like(corr)
	mask[np.triu_indices_from(mask)] = True

	# Set up the matplotlib figure
	fig, ax = plt.subplots()

	# Draw the heatmap with 'sns.heatmap()'
	ax = sns.heatmap(data=corr, mask=mask, annot=True, fmt='.1f', square=True)


	# Do not modify the next two lines
	fig.savefig('heatmap.png')
	return fig

