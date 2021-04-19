import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
	# Read data from file
	df = pd.read_csv('epa-sea-level.csv')


	# Create scatter plot
	df.plot(kind='scatter',
			x='Year',
			y='CSIRO Adjusted Sea Level',
			figsize=(15,9),
			xlabel='Year',
			ylabel='Sea Level (inches)',
			title='Rise in Sea Level'
			)
	# Create first line of best fit
	stat = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
	line_of_best_fit_y = [(stat.intercept + stat.slope * year) for year in range(1880, 2051)]

	plt.plot(range(1880, 2051), line_of_best_fit_y, 'r-', label='line of prediction')

	# Create second line of best fit
	stat_sec = linregress(df.loc[df['Year'] > 2000]['Year'], df.loc[df['Year'] > 2000]['CSIRO Adjusted Sea Level'])
	sec_line_of_best_fit_y = [(stat_sec.intercept + stat_sec.slope * year) for year in range(2000, 2051)]

	plt.plot(range(2000, 2051), sec_line_of_best_fit_y, 'rv', label='2nd line of prediction')
	# Add labels and title
	#inline 15-17


	# Save plot and return data for testing (DO NOT MODIFY)
	plt.savefig('sea_level_plot.png')
	return plt.gca()
