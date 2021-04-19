import numpy as np


def calculate(lst):
	calculations = dict()

	if len(lst) < 9: raise ValueError('List must contain nine numbers')
	arr = np.array(lst)
	arr_mean = [np.mean(arr).tolist()]
	arr_var = [np.var(arr).tolist()]
	arr_std = [np.std(arr).tolist()]
	arr_max = [np.max(arr).tolist()]
	arr_min = [np.min(arr).tolist()]
	arr_sum = [np.sum(arr).tolist()]

	arr = arr.reshape((3,3))
	for i in range(2):
		arr_mean.insert(i, np.mean(arr, axis=i).tolist())
		arr_var.insert(i, np.var(arr, axis=i).tolist())
		arr_std.insert(i, np.std(arr, axis=i).tolist())
		arr_max.insert(i, np.max(arr, axis=i).tolist())
		arr_min.insert(i, np.min(arr, axis=i).tolist())
		arr_sum.insert(i, np.sum(arr, axis=i).tolist())

	calculations['mean'] = arr_mean
	calculations['variance'] = arr_var
	calculations['standard deviation'] = arr_std
	calculations['max'] = arr_max
	calculations['min'] = arr_min
	calculations['sum'] = arr_sum

	return calculations


