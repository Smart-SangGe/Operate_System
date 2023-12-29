import a


def ComputePageFaultRate(
    page_frame_lenth: int, page_reference_list: list, mode: int = 0
) -> float:
    page_frame_list = [-1] * page_frame_lenth
    hit_count = 0

    if mode not in [0, 1, 2, 3, 4]:
        raise ValueError("Invalid mode")

    algorithm_instance = PageReplacementAlgorithmFactory.create_algorithm(
        mode, page_frame_list, page_reference_list
    )

    # Hit or miss is determined by replacement algorithm
    for i in page_reference_list:
        page_frame_list = algorithm_instance.replace(i)

    hit_count = algorithm_instance.hit_count

    fault_rate = 1 - (hit_count / len(page_reference_list))
    return fault_rate


class PageReplacementAlgorithm:
    def __init__(self):
        # Initialize any required data structures for the algorithm
        self.hit_count = 0
        pass


class PageReplacementAlgorithmFactory:
    @staticmethod
    def create_algorithm(mode: int, *args, **kwargs) -> PageReplacementAlgorithm:
        if mode == 0:
            # Return an instance of the OPT algorithm class
            return OPTAlgorithm(*args, **kwargs)
        elif mode == 1:
            # Return an instance of the FIFO algorithm class
            return FIFOAlgorithm(*args, **kwargs)
        elif mode == 2:
            # Return an instance of the LRU algorithm class
            return LRUAlgorithm(*args, **kwargs)
        elif mode == 3:
            # Return an instance of the LFU algorithm class
            return LFUAlgorithm(*args, **kwargs)
        elif mode == 4:
            # Return an instance of the CLOCK algorithm class
            return CLOCKAlgorithm(*args, **kwargs)


# Implement specific algorithm classes and their replace methods
class OPTAlgorithm(PageReplacementAlgorithm):
    def __init__(self, page_frame_list: list, page_reference_list: list):
        super().__init__()
        self.page_frame_list = page_frame_list
        self.page_reference_list = page_reference_list
        self.counter = 0

        # compute all return value
        self.return_list = []
        counter_list = [-1] * len(self.page_frame_list)
        for i in range(len(self.page_reference_list)):
            if self.page_reference_list[i] not in self.page_frame_list:
                counter_list = [float("inf")] * len(self.page_frame_list)

                for j in range(len(self.page_frame_list)):
                    if self.page_frame_list[j] in self.page_reference_list[i + 1 :]:
                        counter_list[j] = self.page_reference_list.index(
                            self.page_frame_list[j], i + 1
                        )

                # 找到最远的或未来不会被引用的页面
                max_index = counter_list.index(max(counter_list))
                self.page_frame_list[max_index] = self.page_reference_list[i]

                # 添加当前状态的副本
                self.return_list.append(self.page_frame_list[:])

    def replace(self, element: int):
        # Implement OPT algorithm logic

        counter = self.counter
        self.counter += 1
        try:
            return self.return_list[counter]
        except:
            return self.return_list[counter - 1]


class FIFOAlgorithm(PageReplacementAlgorithm):
    def __init__(self, page_frame_list: list, page_reference_list: list):
        super().__init__()
        self.page_frame_list = page_frame_list
        self.page_reference_list = page_reference_list

    def replace(self, element: int):
        # Implement FIFO algorithm logic
        if element not in self.page_frame_list:
            # pop first element, push new element at the end
            page_frame_list = self.page_frame_list[1:]
            page_frame_list.append(element)
            self.page_frame_list = page_frame_list
            self.hit_count += 1

        return self.page_frame_list


class LRUAlgorithm(PageReplacementAlgorithm):
    def __init__(self, page_frame_list: list, page_reference_list: list):
        super().__init__()
        self.page_frame_list = page_frame_list
        self.page_reference_list = page_reference_list
        self.index = 0

    def replace(self, element: int):
        # Implement LRU algorithm logic

        # Because there is no way to know the number of hits,
        # it needs to be tracked within the method
        while element != self.page_reference_list[self.index]:
            # pop used element, then store in the end of list
            used_element = self.page_reference_list[self.index]
            self.page_frame_list.pop(self.page_frame_list.index(used_element))
            self.page_frame_list.append((used_element))

            # At this time, the page hits and the counter increases by one.
            self.index += 1

        # Find the calling index and prepare to replace
        self.page_frame_list[0] = element
        return self.page_frame_list


class LFUAlgorithm(PageReplacementAlgorithm):
    def __init__(self, page_frame_list: list, page_reference_list: list):
        super().__init__()
        self.page_frame_list = page_frame_list
        self.page_reference_list = page_reference_list
        self.counter = 0
        # Initialize any data structures required for LFU
        # 初始化页面频率字典和页面最后访问索引字典
        self.frequency_dict = {page: 0 for page in self.page_frame_list}
        self.last_used_index = {page: -1 for page in self.page_frame_list}

    def replace(self, element: int):
        # Implement LFU algorithm logic
        # 检查元素是否已经在页框列表中
        if element in self.page_frame_list:
            # 增加频率计数
            self.frequency_dict[element] += 1
            # 更新最后访问索引
            self.last_used_index[element] = self.page_reference_list.index(element)
        else:
            # 如果页框列表未满，添加元素
            if len(self.page_frame_list) < len(self.frequency_dict):
                self.page_frame_list.append(element)
                self.frequency_dict[element] = 1
                self.last_used_index[element] = self.page_reference_list.index(element)
            else:
                # 找出频率最低且最早访问的页面
                least_frequently_used = min(
                    self.frequency_dict,
                    key=lambda x: (self.frequency_dict[x], self.last_used_index[x]),
                )
                # 替换页面
                index_to_replace = self.page_frame_list.index(least_frequently_used)
                self.page_frame_list[index_to_replace] = element
                # 更新频率和最后访问索引
                self.frequency_dict.pop(least_frequently_used)
                self.last_used_index.pop(least_frequently_used)
                self.frequency_dict[element] = 1
                self.last_used_index[element] = self.page_reference_list.index(element)

        return self.page_frame_list


class CLOCKAlgorithm(PageReplacementAlgorithm):
    def __init__(self, page_frame_list: list, page_reference_list: list):
        super().__init__()
        self.page_frame_list = page_frame_list
        self.page_reference_list = page_reference_list
        self.counter = 0

    def replace(self, element: int):
        # Implement CLOCK algorithm logic
        pass


if __name__ == "__main__":
    page_reference_list = a.GenChar(100, 10)
    # page_reference_list = [3, 3, 3, 3, 2, 2, 2, 1, 3, 3]
    print(page_reference_list)
    PAGE_FRAME_LENTH = 5
    page_fault_rate = ComputePageFaultRate(
        PAGE_FRAME_LENTH, page_reference_list, mode=0
    )
    print(page_fault_rate)
