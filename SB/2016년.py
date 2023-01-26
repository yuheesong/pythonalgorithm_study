from datetime import datetime
def solution(a, b):
    datetime_data = datetime(2016,a,b)
    date_dict = {0:'MON',1:'TUE',2:'WED',3:'THU',4:'FRI',5:'SAT',6:'SUN'}
    return date_dict[datetime_data.weekday()]

print(solution(5,24))