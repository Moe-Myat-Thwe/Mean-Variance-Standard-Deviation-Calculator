import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    ls = np.array(list)
    ls = ls.reshape(3,3)


    mean_row = np.mean(ls, axis=1)
    mean_column = np.mean(ls, axis=0)
    mean_flattened = np.mean(ls)

    var_row = np.var(ls, axis=1)
    var_column = np.var(ls, axis=0)
    var_flattened = np.var(ls)

    std_row = np.std(ls, axis=1)
    std_column = np.std(ls, axis=0)
    std_flattened = np.std(ls)

    max_row = np.max(ls, axis=1)
    max_column = np.max(ls, axis=0)
    max_flattened = np.max(ls)

    min_row = np.min(ls, axis=1)
    min_column = np.min(ls, axis=0)
    min_flattened = np.min(ls)

    sum_row = np.sum(ls, axis=1)
    sum_column = np.sum(ls, axis=0)
    sum_flattened = np.sum(ls)

    results = {'mean': [mean_column, mean_row, mean_flattened],
               'variance': [var_column, var_row, var_flattened],
               'standard deviation': [std_column, std_row, std_flattened],
               'max': [max_column, max_row, max_flattened],
               'min': [min_column, min_row, min_flattened],
               'sum': [sum_column, sum_row, sum_flattened] }

    fix_results = {}
    for key, value_list in results.items():
        fix_values = []
        for item in value_list:
            fix_values.append(item.tolist())
            fix_results[key] = fix_values
    return fix_results


