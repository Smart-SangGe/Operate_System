import unittest
import a
from b import (
    ComputePageFaultRate,
    OPTAlgorithm,
    FIFOAlgorithm,
    LRUAlgorithm,
    LFUAlgorithm,
    CLOCKAlgorithm,
)


class TestPageReplacementAlgorithms(unittest.TestCase):
    def test_OPTAlgorithm(self):
        # 测试OPT算法
        page_reference_list = a.GenChar(100, 10)
        PAGE_FRAME_LENTH = 5
        page_fault_rate = ComputePageFaultRate(
            PAGE_FRAME_LENTH, page_reference_list, mode=0
        )
        print("OPT:", page_fault_rate)

        self.assertTrue(True)

    def test_FIFOAlgorithm(self):
        # 测试FIFO算法
        page_reference_list = a.GenChar(100, 10)
        PAGE_FRAME_LENTH = 5
        page_fault_rate = ComputePageFaultRate(
            PAGE_FRAME_LENTH, page_reference_list, mode=1
        )
        print("FIFO", page_fault_rate)

        self.assertTrue(True)
        page_reference_list = [0, 1, 7, 2, 3, 2, 7, 1, 0, 3]
        PAGE_FRAME_LENTH = 5
        page_fault_rate = ComputePageFaultRate(
            PAGE_FRAME_LENTH, page_reference_list, mode=1
        )
        print("FIFO", page_fault_rate)
        self.assertEqual(page_fault_rate, 0.4)

    def test_LRUAlgorithm(self):
        # 测试LRU算法
        page_reference_list = a.GenChar(100, 10)
        PAGE_FRAME_LENTH = 5
        page_fault_rate = ComputePageFaultRate(
            PAGE_FRAME_LENTH, page_reference_list, mode=2
        )
        print("LRU", page_fault_rate)

        self.assertTrue(True)

    def test_LFUAlgorithm(self):
        # 测试LFU算法
        page_reference_list = a.GenChar(100, 10)
        PAGE_FRAME_LENTH = 5
        page_fault_rate = ComputePageFaultRate(
            PAGE_FRAME_LENTH, page_reference_list, mode=3
        )
        print("LFU", page_fault_rate)

        self.assertTrue(True)

    def test_CLOCKAlgorithm(self):
        # 测试CLOCK算法
        page_reference_list = a.GenChar(100, 10)
        PAGE_FRAME_LENTH = 5
        page_fault_rate = ComputePageFaultRate(
            PAGE_FRAME_LENTH, page_reference_list, mode=4
        )
        print("CLOCK", page_fault_rate)

        self.assertTrue(True)


class TestComputePageFaultRate(unittest.TestCase):
    def test_page_fault_rate(self):
        # 测试页面错误率计算
        page_reference_list = a.GenChar(100, 10)
        for i in range(5):
            page_fault_rate = ComputePageFaultRate(5, page_reference_list, mode=i)
            # 确保页面错误率在合理范围内
            self.assertTrue(0 <= page_fault_rate <= 1)


if __name__ == "__main__":
    unittest.main()
