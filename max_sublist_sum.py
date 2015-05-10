def max_sublist_sum(input_list):
    max_sum = 0
    cur_sum = 0
    curi = 0
    starti = 0
    endi = 0
    for index, num in enumerate(input_list):
        if cur_sum+num > 0:
            cur_sum += num
        else:
            cur_sum = 0
            curi = index+1
        if cur_sum > max_sum:
            max_sum = cur_sum
            starti = curi
            endi = index+1
    print "list is:", input_list
    print "sublist with largest sum is:", input_list[starti:endi]

max_sublist_sum([5, 4, 9, 18, 15])
max_sublist_sum([-15, -20, -7, -1, -8])
max_sublist_sum([-16, 10, 16, 17, -4])
max_sublist_sum([6, 12, 6, -19, 1, 13, -16, 7, 4, -18, -8])
