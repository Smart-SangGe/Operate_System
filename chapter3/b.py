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
        algorithm_instance.replace(i)

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


# mode 0
class OPTAlgorithm(PageReplacementAlgorithm):
    def __init__(self, page_frame_list: list, page_reference_list: list):
        super().__init__()
        self.page_frame_list = page_frame_list
        self.page_reference_list = page_reference_list
        self.counter = 0

        # compute all return value
        self.return_list = []
        counter_list = [float("inf")] * len(self.page_frame_list)

        for i in range(len(self.page_reference_list)):
            if self.page_reference_list[i] not in self.page_frame_list:
                # Calculate the next reference time of each page
                for j in range(len(self.page_frame_list)):
                    if self.page_frame_list[j] in self.page_reference_list[i + 1 :]:
                        counter_list[j] = self.page_reference_list.index(
                            self.page_frame_list[j], i + 1
                        )
                    else:
                        counter_list[j] = float("inf")

                # 找到最远的或未来不会被引用的页面
                max_index = counter_list.index(max(counter_list))
                self.page_frame_list[max_index] = self.page_reference_list[i]
                # 添加当前状态的副本
                self.return_list.append(self.page_frame_list[:])

    def replace(self, element: int):
        # Implement OPT algorithm logic
        if element not in self.page_frame_list:
            if self.counter < len(self.return_list):
                self.page_frame_list = self.return_list[self.counter]
            else:
                self.page_frame_list = self.page_frame_list
            self.counter += 1
        else:
            # 如果元素已在页面帧列表中，不需要替换
            self.hit_count += 1


# mode 1
class FIFOAlgorithm(PageReplacementAlgorithm):
    def __init__(self, page_frame_list: list, page_reference_list: list):
        super().__init__()
        self.page_frame_list = page_frame_list
        self.page_reference_list = page_reference_list

    def replace(self, element: int):
        # Implement FIFO algorithm logic
        if element not in self.page_frame_list:
            # pop first element, push new element at the end
            self.page_frame_list.pop(0)
            self.page_frame_list.append(element)
        else:
            self.hit_count += 1


# mode 2
class LRUAlgorithm(PageReplacementAlgorithm):
    def __init__(self, page_frame_list: list, page_reference_list: list):
        super().__init__()
        self.page_frame_list = page_frame_list
        self.page_reference_list = page_reference_list
        self.index = 0

    def replace(self, element: int):
        # Implement LRU algorithm logic

        if element in self.page_frame_list:
            self.hit_count += 1

            index = self.page_frame_list.index(element)
            self.page_frame_list.pop(index)
            self.page_frame_list.append(element)

        else:
            self.page_frame_list.pop(0)
            self.page_frame_list.append(element)


# mode 3
class LFUAlgorithm(PageReplacementAlgorithm):
    def __init__(self, page_frame_list: list, page_reference_list: list):
        super().__init__()
        self.page_frame_list = page_frame_list
        self.page_reference_list = page_reference_list
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
            # error here
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


# mode 4
class CLOCKAlgorithm(PageReplacementAlgorithm):
    def __init__(self, page_frame_list: list, page_reference_list: list):
        super().__init__()
        self.page_frame_list = page_frame_list
        self.page_reference_list = page_reference_list
        self.reference_bits = {page: 0 for page in self.page_frame_list}
        self.pointer = 0

    def replace(self, element: int):
        # Implement CLOCK algorithm logic
        if element not in self.page_frame_list:
            while True:
                # 检查当前指针位置的页面
                current_page = self.page_frame_list[self.pointer]

                # 如果使用位为0，则替换此页面
                if self.reference_bits[current_page] == 0:
                    self.page_frame_list[self.pointer] = element
                    self.reference_bits[element] = 1  # 设置新页面的使用位为1
                    # 重置被替换页面的使用位
                    self.reference_bits[current_page] = 0
                    break
                else:
                    # 如果使用位为1，则设置为0并移动指针
                    self.reference_bits[current_page] = 0
                    self.pointer = (self.pointer + 1) % len(self.page_frame_list)
        else:
            # 如果页面已在页框列表中，则更新其使用位
            self.reference_bits[element] = 1
            self.hit_count += 1  # 增加命中计数

        # 移动指针
        self.pointer = (self.pointer + 1) % len(self.page_frame_list)


# mode 5
class SCRAlgorithm(PageReplacementAlgorithm):
    def __init__(self, page_frame_list: list, page_reference_list: list):
        super().__init__()
        self.page_frame_list = page_frame_list
        self.page_reference_list = page_reference_list
        self.counter_list = [0] * len(self.page_frame_list)
        
    def replace(self, element: int):
        raise ValueError("Unfinish")

if __name__ == "__main__":
    # page_reference_list = a.GenChar(100, 10)
    page_reference_list = [0, 1, 7, 2, 3, 2, 7, 1, 0, 3]
    print(page_reference_list)
    PAGE_FRAME_LENTH = 4
    page_fault_rate = ComputePageFaultRate(
        PAGE_FRAME_LENTH, page_reference_list, mode=1
    )
    print(page_fault_rate)
