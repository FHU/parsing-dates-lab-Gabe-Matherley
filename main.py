#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    if month == 'January':
        return '01'
    if month == 'February':
        return '02'
    if month == 'March':
        return '03'
    if month == 'April':
        return '04'
    if month == 'May':
        return '05'
    if month == 'June':
        return '06'
    if month == 'July':
        return '07'
    if month == 'August':
        return '08'
    if month == 'September':
        return '09'
    if month == 'October':
        return '10'
    if month == 'November':
        return '11'
    if month == 'December':
        return '12'

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    sep_dates = user_string.split(' ')
    month = parse_month(sep_dates[0])
    day = sep_dates[1].replace(',','')
    year = sep_dates[2]
    if len(day) == 1:
        day = '0' + day
    return f"{month}/{day}/{year}"

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    print(parse_date(user_string))
