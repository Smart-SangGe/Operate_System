import a
import b

if __name__ == "__main__":
    # 为两个进程生成页面引用序列
    page_reference_list_process_1 = a.GenChar(100, 20)
    page_reference_list_process_2 = a.GenChar(100, 20)

    # 使用全局策略，两个进程共享同一个页面框集合
    PAGE_FRAME_LENGTH = 5 * 2  # 页面框数量为原来的两倍
    shared_page_frame_list = [-1] * PAGE_FRAME_LENGTH

    # 创建一个页面置换算法实例，共享页面框集合
    algorithm_instance = b.PageReplacementAlgorithmFactory.create_algorithm(
        4, shared_page_frame_list, []
    )

    # 交替处理两个进程的页面请求
    hit_count_process_1 = 0
    hit_count_process_2 = 0
    for i in range(100):
        algorithm_instance.replace(page_reference_list_process_1[i])
        if algorithm_instance.hit_count > hit_count_process_1 + hit_count_process_2:
            hit_count_process_1 += 1

        algorithm_instance.replace(page_reference_list_process_2[i])
        if algorithm_instance.hit_count > hit_count_process_1 + hit_count_process_2:
            hit_count_process_2 += 1

    # 计算每个进程的页面错误率
    fault_rate_process_1 = 1 - (
        hit_count_process_1 / len(page_reference_list_process_1)
    )
    fault_rate_process_2 = 1 - (
        hit_count_process_2 / len(page_reference_list_process_2)
    )

    print("Global Policy CLOCK Page Fault Rate for Process 1:", fault_rate_process_1)
    print("Global Policy CLOCK Page Fault Rate for Process 2:", fault_rate_process_2)
