# Your code here


def expensive_seq(x, y, z, memory={}):
    # Your code here
    if x <= 0:
        return y + z
    if (x, y, z) in memory:
        return memory[(x, y, z)]

    memory[(x, y, z)] = (expensive_seq(x - 1, y + 1, z, memory) + expensive_seq(x - 2, y + 2, z * 2, memory) +
                         expensive_seq(x - 3, y + 3, z * 3, memory))
    return memory[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
