import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
	# Read data from file
	df = pd.read_csv('epa-sea-level.csv', float_precision='legacy')


	# Create scatter plot
	df.plot(kind='scatter',
			x='Year',
			y='CSIRO Adjusted Sea Level',
			title='Rise in Sea Level',
			xlabel='Year',
			ylabel='Sea Level (inches)'
			)
	# Create first line of best fit
	x = df['Year']
	y = df['CSIRO Adjusted Sea Level']
	stat = linregress(x, y)
	line_of_best_fit_y = [(stat.intercept + stat.slope * year) for year in range(1880, 2050)]

	plt.plot(range(1880, 2050), line_of_best_fit_y, 'r-', label='1st line of prediction')

	# Create second line of best fit
	x = df.loc[df['Year'] >= 2000]['Year']
	y = df.loc[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
	stat_sec = linregress(x, y)
	sec_line_of_best_fit_y = [(stat_sec.intercept + stat_sec.slope * year) for year in range(2000, 2050)]

	plt.plot(range(2000, 2050), sec_line_of_best_fit_y, 'rv', label='2nd line of prediction')
	# Add labels and title

	# Save plot and return data for testing (DO NOT MODIFY)
	plt.savefig('sea_level_plot.png')
	return plt.gca()
