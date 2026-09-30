



def daysInMonth(month: int, year: int) -> int:
    ''' return the amount of days in the month'''
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month == 2: 
            return 29
        else: 
            return days_in_month[month-1]
    else:
        return days_in_month[month-1]
        
def startingDayOfWeek(month: int, year: int) -> int:
    ''' return the first day of the month '''
    centuary = year // 100
    short_year = year % 100
    if month <= 2 :
        new_month = month + 10
        new_year = short_year -2
        first_day = (1+int(2.6*new_month-0.2) - 2*centuary + new_year + int(new_year/4) + int(centuary/4))%7
    else: 
        new_month = month - 2 
        first_day = (1+int(2.6*(new_month)-0.2) - 2*centuary + short_year + int(short_year/4) + int(centuary/4))%7
    return int(first_day+1)
    
def monthCalendarFor(month: int, year: int) -> str:
    ''' return a string when printed looks like previous program'''
    date =1
    month_names = ['','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    if year == 1981 and month == 2:
        start_day = 0
    else:
        start_day = startingDayOfWeek(month, year)
        
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29]
    
    string_list = []
    
    days_title = f'{str(month_names[month])} {str(year)}'
    days_title_string = f'{days_title:^20}'.rstrip()
    
    string_list.append(days_title_string)
    
    string_list.append(f'Su Mo Tu We Th Fr Sa')
    
    list_line1 = []
    list_line1.append('   '*(start_day-1))
    
    list_line2 = []
    for k in range(8-start_day):
        list_line2.append(f'{date:>2}')
        date+=1
        
    list_line1.append(' '.join(list_line2))
    string_list.append(''.join(list_line1))
    
    for i in range (5):
        list = []
        for j in range(7):            
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0  :
                if month == 2:
                    if date <= days_in_month[12]:
                        list.append(f'{date:>2}')
                        date+=1
                elif date <= days_in_month[month-1]:
                    list.append(f'{date:>2}')
                    date+=1
                else: 
                    break
                    
            elif date <= days_in_month[month-1]:
                    list.append(f'{date:>2}')
                    date+=1
            else:
                break
        string_list.append(' '.join(list))
        
    return '\n'.join(string_list) + '\n'
        
        


print(monthCalendarFor(2, 1981))
