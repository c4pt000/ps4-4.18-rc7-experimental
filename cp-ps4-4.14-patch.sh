cp -rfv /opt/ps4-linux/arch/arm/configs/trizeps4_defconfig arch/arm/configs/trizeps4_defconfig

cp -rfv /opt/ps4-linux/arch/arm/mach-pxa/include/mach/trizeps4.h arch/arm/mach-pxa/include/mach/trizeps4.h

cp -rfv /opt/ps4-linux/arch/arm/mach-pxa/trizeps4.c arch/arm/mach-pxa/trizeps4.c

cp -rfv /opt/ps4-linux/arch/x86/include/asm/ps4.h arch/x86/include/asm/ps4.h

cp -rfv /opt/ps4-linux/arch/x86/platform/ps4 arch/x86/platform/ps4

cp -rf /opt/ps4-linux/arch/x86/platform/ps4/* arch/x86/platform/ps4/

cp -rf /opt/ps4-linux/drivers/ps4 drivers/




find . -name '*ps4'
