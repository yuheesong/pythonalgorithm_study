def solution(sizes):
    sort_size = [sorted(sizes[i]) for i in range(len(sizes))]
    min_data = [sort_size[i][0] for i in range(len(sizes))]
    max_data = [sort_size[i][1] for i in range(len(sizes))]
    return max(min_data)*max(max_data)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))