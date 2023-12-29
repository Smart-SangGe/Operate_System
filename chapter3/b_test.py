import unittest
import a
from b import ComputePageFaultRate, OPTAlgorithm, FIFOAlgorithm, LRUAlgorithm, LFUAlgorithm, CLOCKAlgorithm

class TestPageReplacementAlgorithms(unittest.TestCase):
    def test_OPTAlgorithm(self):
        # 测试OPT算法
        page_frame_list = [1, 2, 3]
        page_reference_list = [1, 2, 3, 4, 1, 2, 3, 4]
        algorithm = OPTAlgorithm(page_frame_list, page_reference_list)
        for page in page_reference_list:
            algorithm.replace(page)
        # 在这里添加OPT算法的具体测试断言

    def test_FIFOAlgorithm(self):
        # 测试FIFO算法
        # 在这里添加FIFO算法的具体测试代码和断言
        pass
        
    def test_LRUAlgorithm(self):
        # 测试LRU算法
        # 在这里添加LRU算法的具体测试代码和断言
        pass

    def test_LFUAlgorithm(self):
        # 测试LFU算法
        # 在这里添加LFU算法的具体测试代码和断言
        pass

    def test_CLOCKAlgorithm(self):
        # 测试CLOCK算法
        # 在这里添加CLOCK算法的具体测试代码和断言
        pass

class TestComputePageFaultRate(unittest.TestCase):
    def test_page_fault_rate(self):
        # 测试页面错误率计算
        page_reference_list = a.GenChar(100, 10)
        page_fault_rate = ComputePageFaultRate(5, page_reference_list, mode=0)
        # 确保页面错误率在合理范围内
        self.assertTrue(0 <= page_fault_rate <= 1)

if __name__ == '__main__':
    unittest.main()
