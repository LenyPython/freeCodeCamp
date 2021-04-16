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
df = df[(df['value'] >= df['value'].quantile(0.025)) &
		(df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
	# Draw line plot
	fig, axs = plt.subplots(figsize=(20,9))
	df['value'].plot(xlabel='Date',
					ax=axs,
					ylabel='Page Views',
					style=['r'],
					title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019'
						)
	# Save image and return fig (don't change this part)
	fig.savefig('line_plot.png')
	return fig

def draw_bar_plot():
	# Copy and modify data for monthly bar plot
	df_bar = pd.DataFrame(df.resample('M').mean())
	df_bar['Months'] = df_bar.index.month_name()
	df_bar.index = df_bar.index.year
	df_bar = df_bar.pivot(columns='Months', values='value')
	df_bar = df_bar[['January', 'February','March','April','May','June','July','August','September','October','November','December']]

	# Draw bar plot
	fig, axs = plt.subplots(figsize=(12,9))
	df_bar.plot(kind='bar',
			ax=axs,
			xlabel='Years',
			ylabel='Average Page Views',
			)

	# Save image and return fig (don't change this part)
	fig.savefig('bar_plot.png')
	return fig

def draw_box_plot():
	# Prepare data for box plots (this part is done!)
	df_box = df.copy()
	df_box.reset_index(inplace=True)
	df_box['year'] = [d.year for d in df_box.date]
	df_box['month'] = [d.strftime('%b') for d in df_box.date]

	# Draw box plots (using Seaborn)
	fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12,9))
	#plt.ticklabel_format(useOffset=False)

	sns.boxplot(x="year", y="value", ax=ax1, data=df_box)
	ax1.set_title('Year-wise Box Plot (Trend)')
	ax1.set_ylabel('Page Views')
	ax1.set_xlabel('Year')

	sns.boxplot(x="month", y="value", ax=ax2, data=df_box,
			order=['Jan', 'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oc','Nov','Dec'])
	df_box.index = pd.to_datetime(df_box['month'])
	ax2.set_title('Month-wise Box Plot (Seasonality)')
	ax2.set_ylabel('Page Views')
	ax2.set_xlabel('Month')


	# Save image and return fig (don't change this part)
	fig.savefig('box_plot.png')
	return fig
