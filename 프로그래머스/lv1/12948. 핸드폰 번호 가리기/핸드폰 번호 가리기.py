import re
def solution(phone_number):
    answer = re.sub(phone_number[0:-4],'*'*(len(phone_number)-4),phone_number)
    return answer