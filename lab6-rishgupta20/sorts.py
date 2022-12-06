import random
import time


def selection_sort(l):
    comp = 0
    for i in range(len(l) - 1):
        small_idx = i
        for j in range(i+1, len(l)):
            comp += 1
            if l[j] < l[small_idx]:
                small_idx = j
        temp = l[i]
        l[i] = l[small_idx]
        l[small_idx] = temp
    return comp


def insertion_sort(l):
    comp = 0
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            comp += 1
            if l[j] < l[j-1]:
                temp = l[j-1]
                l[j-1] = l[j]
                l[j] = temp
            else:
                break
    return comp


def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234)

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time()
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)


if __name__ == '__main__':
    main()
