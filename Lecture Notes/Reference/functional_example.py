# example for functionals - functions using functions as parameter

def sort_func(lst, compare_function = lambda x:max(x)):
    if len(lst) == 1:
        return lst
    else:
        mid = len(lst)/2
        return merge(sort_func(lst[:mid], 
    