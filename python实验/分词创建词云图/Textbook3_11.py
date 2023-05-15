for male in range(100):
    for famale in range(100):
        small = 100 - male - famale
        if small > 0 and 5 * male + 3 * famale + small / 3 == 100:
            print('公鸡%d只,母鸡%d只,小鸡%d只'%(male,famale,small))