import a
import b

if __name__ == "__main__":
    # 为第一个进程生成页面引用序列
    page_reference_list_process_1 = a.GenChar(100, 10)
    # 为第二个进程生成页面引用序列
    page_reference_list_process_2 = a.GenChar(100, 10)

    # 页面框数量为原来的两倍
    PAGE_FRAME_LENGTH = 5 * 2

    # 分别计算两个进程的页面错误率
    page_fault_rate_process_1 = b.ComputePageFaultRate(
        PAGE_FRAME_LENGTH, page_reference_list_process_1, mode=4
    )
    page_fault_rate_process_2 = b.ComputePageFaultRate(
        PAGE_FRAME_LENGTH, page_reference_list_process_2, mode=4
    )

    print("CLOCK Page Fault Rate for Process 1:", page_fault_rate_process_1)
    print("CLOCK Page Fault Rate for Process 2:", page_fault_rate_process_2)
