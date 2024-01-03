#include <linux/module.h>
#include <linux/fs.h>
MODULE_LICENSE("GPL");
static struct file_system_type myfs_type = {
    .name = "myfs",
    .owner = THIS_MODULE,
};
MODULE_ALIAS_FS("myfs");
static int __init register_newfs_init(void)
{
    printk("Group 10, Start register_newfs module...");
    return register_filesystem(&myfs_type); // 请同学们自行补充代码。
}
static void __exit register_newfs_exit(void)
{
    printk("Group 10, Exit register_newfs module...");
    unregister_filesystem(&myfs_type);
}
module_init(register_newfs_init);
module_exit(register_newfs_exit);