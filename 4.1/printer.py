def solution(priorities, location):
    answer = 0
    sortedPriorities = sorted(priorities, reverse=True)
    index = 0
    counter = 0
    while True:
        if answer != 0:
            return answer
        if priorities[index] == sortedPriorities[0]:
            counter += 1
            sortedPriorities.pop(0)
            if index == location:
                answer = counter
        index += 1
        index = index % len(priorities)

print(solution([2, 1, 3, 2], 2))