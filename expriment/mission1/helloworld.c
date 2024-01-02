#include <linux/module.h>
MODULE_LICENSE("GPL");
int __init hello_init(void)
{
    printk("hello init, Group 10\n");
    printk("hello,world! Group 10\n");
    return 0;
}
void __exit hello_exit(void)
{
    printk("hello exit, Group 10\n");
}
module_init(hello_init);
module_exit(hello_exit);