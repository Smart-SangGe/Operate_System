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
    for i in page_reference_list:
        # if page not in page frame
        if i not in page_frame_list:
            page_frame_list = algorithm_instance.replace(i)
        else:
            hit_count += 1

    fault_rate = 1 - (hit_count / len(page_reference_list))
    return fault_rate


class PageReplacementAlgorithm:
    def __init__(self):
        # Initialize any required data structures for the algorithm
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


# Implement specific algorithm classes and their replace methods...
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
                counter_list = [float('inf')] * len(self.page_frame_list)

                for j in range(len(self.page_frame_list)):
                    if self.page_frame_list[j] in self.page_reference_list[i + 1:]:
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
        self.counter = 0

    def replace(self, element: int):
        # Implement FIFO algorithm logic
        return self.page_frame_list


class LRUAlgorithm(PageReplacementAlgorithm):
    def __init__(self, page_frame_list: list, page_reference_list: list):
        super().__init__()
        self.page_frame_list = page_frame_list
        self.page_reference_list = page_reference_list
        self.counter = 0

    def replace(self, element: int):
        # Implement LRU algorithm logic
        pass


class LFUAlgorithm(PageReplacementAlgorithm):
    def __init__(self, page_frame_list: list, page_reference_list: list):
        super().__init__()
        self.page_frame_list = page_frame_list
        self.page_reference_list = page_reference_list
        self.counter = 0
        # Initialize any data structures required for LFU
        self.counter_dict = {}

    def replace(self, element: int):
        # Implement LFU algorithm logic
        pass


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
    #page_reference_list = [3, 3, 3, 3, 2, 2, 2, 1, 3, 3]
    print(page_reference_list)
    PAGE_FRAME_LENTH = 5
    page_fault_rate = ComputePageFaultRate(
        PAGE_FRAME_LENTH, page_reference_list, mode=0
    )
    print(page_fault_rate)
