#include <linux/module.h>
MODULE_LICENSE("GPL");
int __init hello_init(void)
{
    printk("hello init\n");
    printk("hello,world!\n");
    return 0;
}
void __exit hello_exit(void)
{
    printk("hello exit\n");
}
module_init(hello_init);
module_exit(hello_exit);