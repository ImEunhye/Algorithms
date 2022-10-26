def solution(record):
    answer = []
    record_dict = {}
    for i in range(len(record)):
        uid = record[i].split()[1]
        
        if len(record[i].split())>2:
            name = record[i].split()[2]
            if uid in record_dict.keys():
                record_dict[uid].append(name)
            else:
                record_dict[uid] = []
                record_dict[uid].append(name)
    
    for rec in record:
        word = rec.split()[0]
        uid = rec.split()[1]
        
        if word == 'Enter':
            answer.append(record_dict[uid][-1]+'님이 들어왔습니다.')
        elif word == 'Leave':
            answer.append(record_dict[uid][-1]+'님이 나갔습니다.')
        
            
        
    return answer