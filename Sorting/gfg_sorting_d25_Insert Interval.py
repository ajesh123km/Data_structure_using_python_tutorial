def insertInterval(intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
        
    res.append(newInterval)

    while i < n:
        res.append(intervals[i])
        i += 1

    return res


if __name__ == "__main__":
    intervals = [[1, 3], [4, 5], [6, 7], [8, 10]]
    newInterval = [5, 6]
    res = insertInterval(intervals, newInterval)
    
    for interval in res:
        print(interval[0], interval[1])
