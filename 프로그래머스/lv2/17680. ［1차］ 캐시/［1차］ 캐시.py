def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = list(map(lambda x: x.lower(), cities))
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        if not city in cache :
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
            answer += 5
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
            
    return answer