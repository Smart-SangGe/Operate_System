import random

N = 30


def GenChar(length: int, N: int) -> list:
    if N <= 1:
        raise ValueError("N must be bigger than 1")
    page_reference_list = []
    current_page = random.randrange(N)

    for _ in range(length):
        pi = random.random()
        if random.random() < pi:
            # 以概率pi引用同一页面
            page_reference_list.append(current_page)
        else:
            # 以等概率选择其他页面
            new_page = random.choice([i for i in range(N) if i != current_page])
            page_reference_list.append(new_page)
            current_page = new_page  # 更新当前页面

    return page_reference_list


if __name__ == "__main__":
    N = input("input N: ")
    try:
        N = int(N)
    except:
        N = 30
    page_reference_list = GenChar(10, N)
    print(page_reference_list)
