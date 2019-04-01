def solution(heights):
    heights.reverse()

    answer = []
    index = 1
    for height in heights:
        index2 = 1
        answer.append(0)
        for height2 in heights:
            if index > index2:
                pass
            elif height < height2:
                answer[index - 1] = len(heights) - index2 + 1
                break
            index2 += 1
        index += 1

    answer.reverse()
    return answer