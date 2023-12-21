import random

N = 30


def GenChar(lenth: int, N: int) -> list:
    page_reference_list = []
    for _ in range(lenth):
        page_reference_list.append(random.randrange(N))

    return page_reference_list


if __name__ == "__main__":
    N = input("input N: ")
    try:
        N = int(N)
    except:
        N = 30
    page_reference_list = GenChar(10, N)
    print(page_reference_list)
