import copy


def check_and_add_in_set(set_name, i, j, l):
    if i >= 0 and j >= 0 and i < l and j < l:
        set_name.add((i, j))
    return


t = int(input())
for _ in range(t):
    l = int(input())
    s_i, s_j = map(int, input().split(' '))
    e_i, e_j = map(int, input().split(' '))
    start_knight = (s_i, s_j)
    end_knight = (e_i, e_j)
    curr_location = {start_knight}
    move_cnt = 0
    while end_knight not in curr_location:
        tmp_set = set()
        for tu in curr_location:
            cl_i, cl_j = tu[0], tu[1]
            check_and_add_in_set(tmp_set, cl_i+1, cl_j+2, l)
            check_and_add_in_set(tmp_set, cl_i+2, cl_j+1, l)
            check_and_add_in_set(tmp_set, cl_i+2, cl_j-1, l)
            check_and_add_in_set(tmp_set, cl_i+1, cl_j-2, l)
            check_and_add_in_set(tmp_set, cl_i-1, cl_j-2, l)
            check_and_add_in_set(tmp_set, cl_i-2, cl_j-1, l)
            check_and_add_in_set(tmp_set, cl_i-2, cl_j+1, l)
            check_and_add_in_set(tmp_set, cl_i-1, cl_j+2, l)
        move_cnt += 1
        curr_location = copy.deepcopy(tmp_set)
    print(move_cnt)
