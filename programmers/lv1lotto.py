def solution(lottos, win_nums):
    answer = []
    _max, _min = 0, 0
    zerocount = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    for i in range(6):
        for j in range(6):
            if lottos[i] == 0:
                zerocount += 1
                break
            elif lottos[i] == win_nums[j]:
                _min += 1
    _max = _min + zerocount
    answer.append(rank[_max])
    answer.append(rank[_min])
    return answer