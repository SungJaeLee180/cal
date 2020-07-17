def addfunc(iter):
    sum_ = 0
    for i in iter:
        sum_ += i
    return sum_

if __name__ == '__main__':
    print('test start')
    assert(addfunc([2, 4, 5]) == 11)
    print('pass')