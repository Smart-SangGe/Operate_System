import random

N = 30


def GenChar(lenth: int, N: int) -> list:
    # Page Reference List
    PRlist = []
    for _ in range(lenth):
        PRlist.append(random.randrange(N))
        
    return PRlist


if __name__ == "__main__":
    N = input("input N: ")
    try:
        N = int(N)
    except:
        N = 30
    PRlist = GenChar(10, N)
    print(PRlist)
