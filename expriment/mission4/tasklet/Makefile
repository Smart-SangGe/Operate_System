ifneq ($(KERNELRELEASE),)
	obj-m := tasklet_intertupt.o
else
	KERNELDIR := /lib/modules/$(shell uname -r)/build
	PWD := $(shell pwd)

default:
	$(MAKE) -C $(KERNELDIR) M=$(PWD) modules
endif

.PHONY: clean
clean:
	-rm -f *.mod.c *.o *.order *.symvers *.ko
