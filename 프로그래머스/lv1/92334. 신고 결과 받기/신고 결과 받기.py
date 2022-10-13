def solution(id_list, report, k):
    answer = []
    report_dict = {}
    reported = {}
    idx = 0
    
    for id_ in id_list:
        report_dict[id_] = []
        reported[id_] = 0
                
    for rep in report:
        if rep.split()[1] not in report_dict[rep.split()[0]]:
            report_dict[rep.split()[0]].append(rep.split()[1])
            reported[rep.split()[1]] += 1
    
    for id_ in id_list:
        cnt = 0
        for i in report_dict[id_]:
            if reported[i] >=k : 
                cnt += 1
        answer.append(cnt)
        idx += 1
        

    return answer