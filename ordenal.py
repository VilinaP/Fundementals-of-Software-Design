def ordinal(num:int) -> str:
    ''' This function is turning a given numbrer into a ordenal word for a number 
    >>> ordinal(1)
    '1st'
    >>> ordinal(2)
    '2nd'
    >>> ordinal(3)
    '3rd'
    >>> ordinal(4)
    '4th'
    >>> ordinal(11)
    '11th'
    '''
    if num == 1:
        return '1st'
    elif num == 2:
        return '2nd'
    elif num == 3:
        return '3rd'
    else:
        return str(num)+'th'
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()