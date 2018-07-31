#!/bin/bash

# README.md
# edit and export your image to "logo-build.ppm" from GIMP or Image authoring program
# must be in this same dir as script
# RHEL variants yum/dnf install netpbm-progs-10.79.00-7.el7.x86_64
# Deb variants sudo apt-get install netpbm 
# nano /etc/default/grub
#for legacy video devices low memory > EGA            vga=0x318
# GRUB_CMDLINE_LINUX = (<- rd.regular-kernel-options-here -> add vga= )      vga=0x318
#for most video devices <= 1920 (1080p)            vga=0x324
# GRUB_CMDLINE_LINUX = (<- rd.regular-kernel-options-here -> add vga= )      vga=0x324
#
# RHEL variants
# grub2-mkconfig -o /boot/grub2/grub.cfg
#
# Debian variants
# update-grub
#
#




#ppmquant 224 logo-build.ppm > my_boot_logo_224.ppm
#pnmnoraw my_boot_logo_224.ppm > my_boot_logo_ascii_224.ppm

# edit this line to the root of your linux source /opt/linux-4.18-rc5    <- Linux source root example
# dont edit "logo_linux_clut224.ppm" file name hardcoded by linux source,  unless logo.c ? is modified

#cp -rf /opt/linux-4.18-rc5/drivers/video/logo/logo_linux_clut224.ppm /opt/linux-4.18-rc5/drivers/video/logo/logo_linux_clut224.ppm.orig


#cd /opt/linux-ver        #edit this line to your kernel source

#run from kernel dir source

cp -rf `$PWD`drivers/video/logo/logo_linux_clut224.ppm `$PWD`drivers/video/logo/logo_linux_clut224.ppm.orig

ppmquant 224 logo-build.ppm > my_boot_logo_224.ppm
pnmnoraw my_boot_logo_224.ppm > my_boot_logo_ascii_224.ppm

cp -v my_boot_logo_ascii_224.ppm `$PWD`drivers/video/logo/logo_linux_clut224.ppm









#kernel build

# for modern systems with more than 16 processing cores edit -j to a higher number for cpu core count
# for debian variant build
# make -j16 deb


# for RHEL variant build ignore comments,
# make -j16 rpm

        #building the kernel rpm's the long , stupid way

        # make -j16 bzImage
        # make -j16 modules
        # make -j16 modules_install
        # make -j16 install
        # make -j16 rpm-pkg

