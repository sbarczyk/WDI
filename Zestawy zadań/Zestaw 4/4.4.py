tab = [[1,2,3,4],
       [5,5,5,5],
       [2,2,1,2],
       [42,24,71,56]]
def calc_col_sum(tab, x):
    sum = 0
    for y in range (len(tab)):
        sum += tab[y][x]
    return sum

def zad(tab):
    column_sums = [calc_col_sum(tab, x) for x in range (len(tab))]
    row_sums = [sum(tab[y]) for y in range (len(tab))]

    max_col = max(column_sums)
    min_row = min(row_sums)
    index_max_col = column_sums.index(max_col)
    index_min_row = row_sums.index(min_row)

    max_ratio = max_col / min_row
    return (max_ratio, index_max_col, index_min_row)

def print_tab(tab):
    for line in tab:
        print(line)
    print("------------")


print_tab(tab)
print(zad(tab))