def findLength(N, A, B):
    n_list = []
    for i in range(0, N):
        a, b = input('Enter x1, x2 for N{}: '.format(i + 1)).split()
        n_list.append([float(a), float(b)])

    res_list = []
    n_list = sorted(n_list)
    var_coord = []
    i = 0
    while i <= len(n_list) - 1:
        if not var_coord:
            # case 1
            if n_list[i][0] <= n_list[i + 1][0] <= n_list[i][1]:
                res_list.append([n_list[i][0], n_list[i + 1][1]])
                var_coord = [n_list[i][0], n_list[i + 1][1]]
                i += 2
            # case 2
            elif n_list[i][0] <= n_list[i + 1][0] and n_list[i][1] >= n_list[i + 1][1]:
                res_list.append([n_list[i][0], n_list[i][1]])
                var_coord = [n_list[i + 1][0], n_list[i + 1][1]]
                i += 1
            # case 3
            elif n_list[i][0] <= n_list[i + 1][0] and n_list[i][1] <= n_list[i + 1][1]:
                res_list.append([n_list[i][0], n_list[i][1]])
                var_coord = [n_list[i + 1][0], n_list[i + 1][1]]
                i += 1

        else:
            if var_coord[0] <= n_list[i][0] <= var_coord[1]:
                res_list.remove(var_coord)
                x1 = var_coord[0]
                var_coord.clear()
                var_coord = [x1, n_list[i][1]]
                res_list.append(var_coord)
                i += 1

            elif var_coord[0] <= n_list[i][0] and var_coord[1] >= n_list[i][1]:
                res_list.remove(var_coord)
                var_coord = [n_list[i][0], n_list[i][1]]
                i += 1

            else:
                res_list.append([n_list[i][0], n_list[i][1]])
                var_coord = [n_list[i][0], n_list[i][1]]
                i += 1

    print(n_list)
    print(res_list)
    sum_length = 0
    for x1, x2 in res_list:
        sum_length += x2 - x1

    print(B - A - sum_length)


'''
1 case
N1 = (0.5, 1.2)
N2 = (0.7, 1.4)
-----------------------
(x1 < y1 and x2 > y1)

2 case
N1 = (0,5, 1.2)
N2 = (0.7, 1.0)
-----------------------
(x1 < y1 and x2 > y2)

3 case
(0.5, 1.2) - ADD
(1.4, 1.7) - NEXT ITERATION
---------------------------
(x1 < y1 and x2 < y1)
'''

if __name__ == '__main__':
    A = float(input('Enter A: '))
    B = float(input('Enter B: '))
    N = int(input('Enter N: '))

    findLength(N, A, B)
