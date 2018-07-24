from numbers_solver.src.numbers_backtracking import NumbersSolver

if __name__ == '__main__':
    n = NumbersSolver()
    target = 952
    numbers = [75, 25, 4, 10, 6, 100]
    solk, iter, ellapsed_time = n.lookup(target, numbers)
    print solk
    print iter
    print '{:.2f}s'.format(ellapsed_time)


