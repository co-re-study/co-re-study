ab_string = list(input())
window_length = 0

for i in range(len(ab_string)):
    if ab_string[i] == 'a':
        window_length += 1
answer = 1000
start_idx = 0

while start_idx < len(ab_string):
    end_idx = start_idx + window_length
    if len(ab_string) >= end_idx:
        slicing_window = ab_string[start_idx:end_idx]

    else:
        slicing_window = ab_string[:end_idx - len(ab_string)] + ab_string[start_idx:len(ab_string)]

    b_cnt = 0
    for i in slicing_window:
        if i == 'b':
            b_cnt += 1
    answer = min(answer, b_cnt)
    start_idx += 1
print(answer)