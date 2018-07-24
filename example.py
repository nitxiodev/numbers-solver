from numbers_solver.src.numbers_backtracking import NumbersSolver

if __name__ == '__main__':
    n = NumbersSolver()
    solk, iter, ellapsed_time = n.lookup(944, [25, 75, 100, 50, 8, 1])
    print solk
    print iter
    print '{:.2f}s'.format(ellapsed_time)
    print len([])