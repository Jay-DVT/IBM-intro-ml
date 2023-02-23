def mean_absolute_error(actual, hat):
    absolute = np.absolute(actual - hat)
    return np.mean(absolute)

def mean_squared_error(actual, hat):
    squared = np.square(actual - hat)
    return np.mean(squared)