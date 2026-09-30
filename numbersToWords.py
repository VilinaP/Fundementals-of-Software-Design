def help_hundred(num: int) -> str:
    '''Takes the 3-digit number and turns in to words. Only up to a hundred
    >>> help_hundred(1)
    'one'
    >>> help_hundred(12)
    'twelve'
    >>> help_hundred(100)
    'one hundred'
    >>> help_hundred(35)
    'thirty-five'
    '''

    first = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    if 1<=num<=9:
        return first[num]
    elif 10<=num<=19:
        return teens[num%10]
    elif 20<=num<=99:
        if num%10 == 0:
            return f'{tens[num%100//10]}'
        else:
            return f'{tens[num%100//10]}-{first[num%10]}'
    elif 100<=num<=999:
        if num%100//10 == 1:
                return f'{first[num%1000//100]} hundred {teens[num%10]}'
        elif num % 100//10 == 0: 
            if num%10 == 0:
                return f'{first[num%1000//100]} hundred'
            else: 
                return f'{first[num%1000//100]} hundred {first[num%10]}'
        elif num % 10 == 0:
            if num%100//10 == 0:
                return f'{first[num%1000//100]} hundred'
            else: 
                return f'{first[num%1000//100]} hundred {tens[num%100//10]}'
        else: 
            return f'{first[num%1000//100]} hundred {tens[num%100//10]}-{first[num%10]}'
    else: 
        return 'Number out of range'

def wordsFromNumber(num: int) -> str:
    ''' Takes the number/integer and turn it into words goes up to 20 digits
    >>> wordsFromNumber(1)
    'one'
    >>> wordsFromNumber(12)
    'twelve'
    >>> wordsFromNumber(100)
    'one hundred'
    >>> wordsFromNumber(35)
    'thirty-five'
    >>> 
    
    '''
    more_zeros = ['','thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion']

    answer_list = []
    
    if num == 0:
        return 'zero'

    count_hundred = 0

    while num > 0:
        temp = num % 1000
        if temp != 0:
            answer_list.insert(0, f'{help_hundred(temp)}')
            if count_hundred >= 1:
                answer_list.insert(1, f'{more_zeros[count_hundred]}')
        count_hundred += 1
        num = num // 1000

    return ' '.join(answer_list)
        


    


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(wordsFromNumber(12000657))