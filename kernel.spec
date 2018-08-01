Name: kernel
Summary: The Linux Kernel
Version: 4.18.0_rc7
Release: 2
License: GPL
Group: System Environment/Kernel
Vendor: The Linux Community
URL: http://www.kernel.org
Source: kernel-4.18.0_rc7.tar.gz
Provides: kernel-drm kernel-4.18.0-rc7
%define __spec_install_post /usr/lib/rpm/brp-compress || :
%define debug_package %{nil}

%description
The Linux Kernel, the operating system core itself

%package headers
Summary: Header files for the Linux kernel for use by glibc
Group: Development/System
Obsoletes: kernel-headers
Provides: kernel-headers = %{version}
%description headers
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%package devel
Summary: Development package for building kernel modules to match the 4.18.0_rc7 kernel
Group: System Environment/Kernel
AutoReqProv: no
%description -n kernel-devel
This package provides kernel headers and makefiles sufficient to build modules
against the 4.18.0_rc7 kernel package.

%prep
%setup -q

%build
make %{?_smp_mflags} KBUILD_BUILD_VERSION=%{release}

%install
mkdir -p %{buildroot}/boot
%ifarch ia64
mkdir -p %{buildroot}/boot/efi
cp $(make image_name) %{buildroot}/boot/efi/vmlinuz-4.18.0-rc7
ln -s efi/vmlinuz-4.18.0-rc7 %{buildroot}/boot/
%else
cp $(make image_name) %{buildroot}/boot/vmlinuz-4.18.0-rc7
%endif
make %{?_smp_mflags} INSTALL_MOD_PATH=%{buildroot} KBUILD_SRC= modules_install
make %{?_smp_mflags} INSTALL_HDR_PATH=%{buildroot}/usr KBUILD_SRC= headers_install
cp System.map %{buildroot}/boot/System.map-4.18.0-rc7
cp .config %{buildroot}/boot/config-4.18.0-rc7
bzip2 -9 --keep vmlinux
mv vmlinux.bz2 %{buildroot}/boot/vmlinux-4.18.0-rc7.bz2
rm -f %{buildroot}/lib/modules/4.18.0-rc7/build
rm -f %{buildroot}/lib/modules/4.18.0-rc7/source
mkdir -p %{buildroot}/usr/src/kernels/4.18.0-rc7
tar cf - --exclude SCCS --exclude BitKeeper --exclude .svn --exclude CVS --exclude .pc --exclude .hg --exclude .git --exclude=.tmp_versions --exclude=*vmlinux* --exclude=*.o --exclude=*.ko --exclude=*.cmd --exclude=Documentation --exclude=.config.old --exclude=.missing-syscalls.d . | tar xf - -C %{buildroot}/usr/src/kernels/4.18.0-rc7
cd %{buildroot}/lib/modules/4.18.0-rc7
ln -sf /usr/src/kernels/4.18.0-rc7 build
ln -sf /usr/src/kernels/4.18.0-rc7 source

%clean
rm -rf %{buildroot}

%post
if [ -x /sbin/installkernel -a -r /boot/vmlinuz-4.18.0-rc7 -a -r /boot/System.map-4.18.0-rc7 ]; then
cp /boot/vmlinuz-4.18.0-rc7 /boot/.vmlinuz-4.18.0-rc7-rpm
cp /boot/System.map-4.18.0-rc7 /boot/.System.map-4.18.0-rc7-rpm
rm -f /boot/vmlinuz-4.18.0-rc7 /boot/System.map-4.18.0-rc7
/sbin/installkernel 4.18.0-rc7 /boot/.vmlinuz-4.18.0-rc7-rpm /boot/.System.map-4.18.0-rc7-rpm
rm -f /boot/.vmlinuz-4.18.0-rc7-rpm /boot/.System.map-4.18.0-rc7-rpm
fi

%preun
if [ -x /sbin/new-kernel-pkg ]; then
new-kernel-pkg --remove 4.18.0-rc7 --rminitrd --initrdfile=/boot/initramfs-4.18.0-rc7.img
elif [ -x /usr/bin/kernel-install ]; then
kernel-install remove 4.18.0-rc7
fi

%postun
if [ -x /sbin/update-bootloader ]; then
/sbin/update-bootloader --remove 4.18.0-rc7
fi

%files
%defattr (-, root, root)
/lib/modules/4.18.0-rc7
%exclude /lib/modules/4.18.0-rc7/build
%exclude /lib/modules/4.18.0-rc7/source
/boot/*

%files headers
%defattr (-, root, root)
/usr/include

%files devel
%defattr (-, root, root)
/usr/src/kernels/4.18.0-rc7
/lib/modules/4.18.0-rc7/build
/lib/modules/4.18.0-rc7/source
