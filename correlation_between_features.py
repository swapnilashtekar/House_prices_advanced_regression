def correlation(x, y):
    '''
    Fill in this function to compute the correlation between the two
    input variables. Each input is either a NumPy array or a Pandas
    Series.
    
    correlation = average of (x in standard units) times (y in standard units)
    
    Remember to pass the argument "ddof=0" to the Pandas std() function!
    '''
    x_std = (x - x.mean()) / (x.std(ddof = 0))
    y_std = (y - y.mean()) /(y.std(ddof = 0))
    
    return (x_std * y_std).mean()