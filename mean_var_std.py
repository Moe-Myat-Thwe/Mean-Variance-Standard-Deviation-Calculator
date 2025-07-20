import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    ls = np.array(list)
    ls = ls.reshape(3,3)

    mean_rows = np.mean(ls, axis=1)
    mean_columns = np.mean(ls, axis=0)

    var_rows = np.var(ls, axis=1)
    var_columns = np.var(ls, axis=0)

    std_rows = np.std(ls, axis=1)
    std_columns = np.std(ls, axis=0)

    max_rows = np.max(ls, axis=1)
    max_columns = np.max(ls, axis=0)

    min_rows = np.min(ls, axis=1)
    min_columns = np.min(ls, axis=0)

    sum_rows = np.sum(ls, axis=1)
    sum_columns = np.sum(ls, axis=0)

    results = {'mean': [mean_columns, mean_rows, np.mean(ls)],
            'variance': [var_columns, var_rows, np.var(ls)],
            'standard deviation': [std_columns, std_rows, np.std(ls)],
            'max': [max_columns, max_rows, np.max(ls)],
            'min': [min_columns, min_rows, np.min(ls)],
            'sum': [sum_columns, sum_rows, np.sum(ls)]}

    fixed_results = {}
    for key, value_list in results.items():
        fixed_list = []
        for item in value_list:
            if isinstance(item, np.ndarray):
                fixed_list.append(item.tolist())
            elif isinstance(item, (np.float64, np.int64)):
                fixed_list.append(item.item())
            else:
                fixed_list.append(item)
        fixed_results[key] = fixed_list
    return fixed_results

