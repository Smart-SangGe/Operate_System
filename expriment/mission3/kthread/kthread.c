#include <linux/kthread.h>
#include <linux/module.h>
#include <linux/delay.h>
MODULE_LICENSE("GPL");
#define BUF_SIZE 20
static struct task_struct *myThread = NULL;
static int print(void *data)
{
    while (!kthread_should_stop())
    {
        printk("Gourp 10, New kthread is running.");
        msleep(2000);
    }
    return 0;
}
static int __init kthread_init(void)
{
    printk("Gourp 10, Create kernel thread!\n");
    myThread = kthread_run(print, NULL, "Group 10 print Thread"); // 请同学们自行补充代码。
    return 0;
}
static void __exit kthread_exit(void)
{
    printk("Gourp 10, Kill new kthread.\n");
    if (myThread)
        kthread_stop(myThread);
}
module_init(kthread_init);
module_exit(kthread_exit);