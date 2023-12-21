# Chapter 3 Memory management

Write a program that will demonstrate the difference between using a local page replacement policy and a global one for the simple case of two processes. You will need a routine that can generate a page reference string based on a statistical model. This model has N states numbered from 0 to N − 1 representing each of the possible page references and a probability pi associated with each state i representing the chance that the next reference is to the same page. Otherwise, the next page reference will be one of the other pages with equal probability.  
(a) Demonstrate that the page reference string-generation routine behaves properly for some small N.  
(b) Compute the page fault rate for a small example in which there is one process and a fixed number of page frames. Explain why the behavior is correct.  
(c) Repeat part (b) with two processes with independent page reference sequences and twice as many page frames as in part (b).  
(d) Repeat part (c) but using a global policy instead of a local one. Also, contrast the per-process page fault rate with that of the local policy approach.  

编写一个程序，用于展示在简单的两个进程情况下，局部页面替换策略和全局页面替换策略之间的区别。你需要一个能够基于统计模型生成页面引用字符串的程序。这个模型有N个状态，从0到N-1编号，代表所有可能的页面引用，每个状态i有一个与之相关的概率pi，代表下一个引用是相同页面的机会。否则，下一个页面引用将等概率地是其他页面。
(a) 为某个小的N值展示页面引用字符串生成程序的正确行为。  
(b) 计算一个小示例中单个进程和固定数量页面帧的页面错误率，并解释为什么这种行为是正确的。  
(c) 重复(b)部分，但使用两个进程，每个进程都有独立的页面引用序列，并且页面帧数量是(b)部分的两倍。  
(d) 重复(c)部分，但使用全局策略而不是局部策略。同时，对比局部策略方法的每个进程的页面错误率和全局策略的页面错误率。  
