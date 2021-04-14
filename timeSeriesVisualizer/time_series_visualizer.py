import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
				parse_dates=True,
				index_col='date')
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &			(df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
	# Draw line plot
	fig, axs = plt.subplots(figsize=(20,9))
	axs = df['value'].plot(xlabel='Date', ylabel='Page Views',style=['r'], title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
	# Save image and return fig (don't change this part)
	fig.savefig('line_plot.png')
	return fig
draw_line_plot()

def draw_bar_plot():
	# Copy and modify data for monthly bar plot
	df_bar = df.copy()
	df_bar = df_bar.reindex(df_bar.index)



	print(df_bar)
	# Draw bar plot
	fig, axs = plt.subplots(figsize=(12,16))
	axs = df_bar.plot(kind='bar',
			xlablel='Years',
			ylablel='Average Page Views',
			)

	# Save image and return fig (don't change this part)
	fig.savefig('bar_plot.png')
	return fig
draw_bar_plot()

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
