%define prefix %{_prefix}/kerberos

Summary: The Kerberos network authentication system.
Name: krb5
Version: 1.2.2
Release: 4
Source0: krb5-%{version}.tar.gz
Source1: kpropd.init
Source2: krb524d.init
Source3: kadmind.init
Source4: krb5kdc.init
Source5: krb5.conf
Source6: krb5.sh
Source7: krb5.csh
Source8: kdcrotate
Source9: kdc.conf
Source10: kadm5.acl
Source11: krsh
Source12: krlogin
Source13: eklogin.xinetd
Source14: klogin.xinetd
Source15: kshell.xinetd
Source16: krb5-telnet.xinetd
Source17: gssftp.xinetd
Source18: krb5server.init
Source19: statglue.c
Patch0: krb5-1.1-db.patch
Patch1: krb5-1.1.1-tiocgltc.patch
Patch2: krb5-1.1.1-libpty.patch
Patch3: krb5-1.1.1-fixinfo.patch
Patch4: krb5-1.1.1-manpages.patch
Patch5: krb5-1.1.1-netkitr.patch
Patch6: krb5-1.2-rlogind.patch
Patch7: krb5-1.2-ksu.patch
Patch8: krb5-1.2-ksu.options.patch
Patch9: krb5-1.2-ksu.man.patch
Patch10: krb5-1.2-quiet.patch
Patch11: krb5-1.1.1-brokenrev.patch
Patch12: krb5-1.2-spelling.patch
Patch13: krb5-1.2.1-term.patch
Patch14: krb5-1.2.1-passive.patch
Patch15: krb5-1.2.1-forward.patch
Patch16: krb5-1.2.1-heap.patch
Patch17: krb5-1.2.2-wragg.patch
Patch18: krb5-1.2.2-statglue.patch
Copyright: MIT, freely distributable.
URL: http://web.mit.edu/kerberos/www/
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-root
Prereq: grep, info, sh-utils, /sbin/install-info
BuildPrereq: bison, e2fsprogs-devel, flex, gzip, libtermcap-devel, rsh, texinfo, tar, tcl

%description
Kerberos V5 is a trusted-third-party network authentication system,
which can improve your network's security by eliminating the insecure
practice of cleartext passwords.

%package devel
Summary: Development files needed for compiling Kerberos 5 programs.
Group: Development/Libraries
Requires: %{name}-libs = %{version}

%description devel
Kerberos is a network authentication system.  The krb5-devel package
contains the header files and libraries needed for compiling Kerberos
5 programs. If you want to develop Kerberos-aware programs, you'll
need to install this package.

%package libs
Summary: The shared libraries used by Kerberos 5.
Group: System Environment/Libraries
Prereq: grep, /sbin/ldconfig, sh-utils
Obsoletes: krb5-configs

%description libs
Kerberos is a network authentication system.  The krb5-libs package
contains the shared libraries needed by Kerberos 5.  If you're using
Kerberos, you'll need to install this package.

%package server
Group: System Environment/Daemons
Summary: The server programs for Kerberos 5.
Requires: %{name}-libs = %{version}, %{name}-workstation = %{version}
Prereq: grep, /sbin/install-info, /bin/sh, sh-utils

%description server
Kerberos is a network authentication system.  The krb5-server package
contains the programs that must be installed on a Kerberos 5 server.
If you're installing a Kerberos 5 server, you need to install this
package (in other words, most people should NOT install this
package).

%package workstation
Summary: Kerberos 5 programs for use on workstations.
Group: System Environment/Base
Requires: %{name}-libs = %{version}
Prereq: grep, /sbin/install-info, /bin/sh, sh-utils

%description workstation
Kerberos is a network authentication system.  The krb5-workstation
package contains the basic Kerberos programs (kinit, klist, kdestroy,
kpasswd) as well as kerberized versions of Telnet and FTP.  If your
network uses Kerberos, this package should be installed on every
workstation.

%changelog
* Fri Mar 30 2001 Nalin Dahyabhai <nalin@redhat.com>
- add in glue code to make sure that libkrb5 continues to provide a
  weak copy of stat()

* Thu Mar 15 2001 Nalin Dahyabhai <nalin@redhat.com>
- build alpha with -O0 for now

* Thu Mar  8 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix the kpropd init script

* Mon Mar  5 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.2.2, which fixes some bugs relating to empty ETYPE-INFO
- re-enable optimization on Alpha

* Thu Feb  8 2001 Nalin Dahyabhai <nalin@redhat.com>
- build alpha with -O0 for now
- own %{_var}/kerberos

* Tue Feb  6 2001 Nalin Dahyabhai <nalin@redhat.com>
- own the directories which are created for each package (#26342)

* Tue Jan 23 2001 Nalin Dahyabhai <nalin@redhat.com>
- gettextize init scripts

* Fri Jan 19 2001 Nalin Dahyabhai <nalin@redhat.com>
- add some comments to the ksu patches for the curious
- re-enable optimization on alphas

* Mon Jan 15 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix krb5-send-pr (#18932) and move it from -server to -workstation
- buildprereq libtermcap-devel
- temporariliy disable optimization on alphas
- gettextize init scripts

* Tue Dec  5 2000 Nalin Dahyabhai <nalin@redhat.com>
- force -fPIC

* Fri Dec  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Tue Oct 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- add bison as a BuildPrereq (#20091)

* Mon Oct 30 2000 Nalin Dahyabhai <nalin@redhat.com>
- change /usr/dict/words to /usr/share/dict/words in default kdc.conf (#20000)

* Thu Oct  5 2000 Nalin Dahyabhai <nalin@redhat.com>
- apply kpasswd bug fixes from David Wragg

* Wed Oct  4 2000 Nalin Dahyabhai <nalin@redhat.com>
- make krb5-libs obsolete the old krb5-configs package (#18351)
- don't quit from the kpropd init script if there's no principal database so
  that you can propagate the first time without running kpropd manually
- don't complain if /etc/ld.so.conf doesn't exist in the -libs %post

* Tue Sep 12 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix credential forwarding problem in klogind (goof in KRB5CCNAME handling)
  (#11588)
- fix heap corruption bug in FTP client (#14301)

* Wed Aug 16 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix summaries and descriptions
- switched the default transfer protocol from PORT to PASV as proposed on
  bugzilla (#16134), and to match the regular ftp package's behavior

* Wed Jul 19 2000 Jeff Johnson <jbj@redhat.com>
- rebuild to compress man pages.

* Sat Jul 15 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Fri Jul 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- disable servers by default to keep linuxconf from thinking they need to be
  started when they don't

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Nalin Dahyabhai <nalin@redhat.com>
- change cleanup code in post to not tickle chkconfig
- add grep as a Prereq: for -libs

* Thu Jul  6 2000 Nalin Dahyabhai <nalin@redhat.com>
- move condrestarts to postun
- make xinetd configs noreplace
- add descriptions to xinetd configs
- add /etc/init.d as a prereq for the -server package
- patch to properly truncate $TERM in krlogind

* Fri Jun 30 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.2.1
- back out Tom Yu's patch, which is a big chunk of the 1.2 -> 1.2.1 update
- start using the official source tarball instead of its contents

* Thu Jun 29 2000 Nalin Dahyabhai <nalin@redhat.com>
- Tom Yu's patch to fix compatibility between 1.2 kadmin and 1.1.1 kadmind
- pull out 6.2 options in the spec file (sonames changing in 1.2 means it's not
  compatible with other stuff in 6.2, so no need)

* Wed Jun 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- tweak graceful start/stop logic in post and preun

* Mon Jun 26 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to the 1.2 release
- ditch a lot of our patches which went upstream
- enable use of DNS to look up things at build-time
- disable use of DNS to look up things at run-time in default krb5.conf
- change ownership of the convert-config-files script to root.root
- compress PS docs
- fix some typos in the kinit man page
- run condrestart in server post, and shut down in preun

* Mon Jun 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- only remove old krb5server init script links if the init script is there

* Sat Jun 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- disable kshell and eklogin by default

* Thu Jun 15 2000 Nalin Dahyabhai <nalin@redhat.com>
- patch mkdir/rmdir problem in ftpcmd.y
- add condrestart option to init script
- split the server init script into three pieces and add one for kpropd

* Wed Jun 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- make sure workstation servers are all disabled by default
- clean up krb5server init script

* Fri Jun  9 2000 Nalin Dahyabhai <nalin@redhat.com>
- apply second set of buffer overflow fixes from Tom Yu
- fix from Dirk Husung for a bug in buffer cleanups in the test suite
- work around possibly broken rev binary in running test suite
- move default realm configs from /var/kerberos to %{_var}/kerberos

* Tue Jun  6 2000 Nalin Dahyabhai <nalin@redhat.com>
- make ksu and v4rcp owned by root

* Sat Jun  3 2000 Nalin Dahyabhai <nalin@redhat.com>
- use %%{_infodir} to better comply with FHS
- move .so files to -devel subpackage
- tweak xinetd config files (bugs #11833, #11835, #11836, #11840)
- fix package descriptions again

* Wed May 24 2000 Nalin Dahyabhai <nalin@redhat.com>
- change a LINE_MAX to 1024, fix from Ken Raeburn
- add fix for login vulnerability in case anyone rebuilds without krb4 compat
- add tweaks for byte-swapping macros in krb.h, also from Ken
- add xinetd config files
- make rsh and rlogin quieter
- build with debug to fix credential forwarding
- add rsh as a build-time req because the configure scripts look for it to
  determine paths

* Wed May 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix config_subpackage logic

* Tue May 16 2000 Nalin Dahyabhai <nalin@redhat.com>
- remove setuid bit on v4rcp and ksu in case the checks previously added
  don't close all of the problems in ksu
- apply patches from Jeffrey Schiller to fix overruns Chris Evans found
- reintroduce configs subpackage for use in the errata
- add PreReq: sh-utils

* Mon May 15 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix double-free in the kdc (patch merged into MIT tree)
- include convert-config-files script as a documentation file

* Wed May 03 2000 Nalin Dahyabhai <nalin@redhat.com>
- patch ksu man page because the -C option never works
- add access() checks and disable debug mode in ksu
- modify default ksu build arguments to specify more directories in CMD_PATH
  and to use getusershell()

* Wed May 03 2000 Bill Nottingham <notting@redhat.com>
- fix configure stuff for ia64

* Mon Apr 10 2000 Nalin Dahyabhai <nalin@redhat.com>
- add LDCOMBINE=-lc to configure invocation to use libc versioning (bug #10653)
- change Requires: for/in subpackages to include %{version}

* Wed Apr 05 2000 Nalin Dahyabhai <nalin@redhat.com>
- add man pages for kerberos(1), kvno(1), .k5login(5)
- add kvno to -workstation

* Mon Apr 03 2000 Nalin Dahyabhai <nalin@redhat.com>
- Merge krb5-configs back into krb5-libs.  The krb5.conf file is marked as
  a %%config file anyway.
- Make krb5.conf a noreplace config file.

* Thu Mar 30 2000 Nalin Dahyabhai <nalin@redhat.com>
- Make klogind pass a clean environment to children, like NetKit's rlogind does.

* Wed Mar 08 2000 Nalin Dahyabhai <nalin@redhat.com>
- Don't enable the server by default.
- Compress info pages.
- Add defaults for the PAM module to krb5.conf

* Mon Mar 06 2000 Nalin Dahyabhai <nalin@redhat.com>
- Correct copyright: it's exportable now, provided the proper paperwork is
  filed with the government.

* Fri Mar 03 2000 Nalin Dahyabhai <nalin@redhat.com>
- apply Mike Friedman's patch to fix format string problems
- don't strip off argv[0] when invoking regular rsh/rlogin

* Thu Mar 02 2000 Nalin Dahyabhai <nalin@redhat.com>
- run kadmin.local correctly at startup

* Mon Feb 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- pass absolute path to kadm5.keytab if/when extracting keys at startup

* Sat Feb 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix info page insertions

* Wed Feb  9 2000 Nalin Dahyabhai <nalin@redhat.com>
- tweak server init script to automatically extract kadm5 keys if
  /var/kerberos/krb5kdc/kadm5.keytab doesn't exist yet
- adjust package descriptions

* Thu Feb  3 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix for potentially gzipped man pages

* Fri Jan 21 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix comments in krb5-configs

* Fri Jan  7 2000 Nalin Dahyabhai <nalin@redhat.com>
- move /usr/kerberos/bin to end of PATH

* Tue Dec 28 1999 Nalin Dahyabhai <nalin@redhat.com>
- install kadmin header files

* Tue Dec 21 1999 Nalin Dahyabhai <nalin@redhat.com>
- patch around TIOCGTLC defined on alpha and remove warnings from libpty.h
- add installation of info docs
- remove krb4 compat patch because it doesn't fix workstation-side servers

* Mon Dec 20 1999 Nalin Dahyabhai <nalin@redhat.com>
- remove hesiod dependency at build-time

* Sun Dec 19 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- rebuild on 1.1.1

* Thu Oct  7 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- clean up init script for server, verify that it works [jlkatz]
- clean up rotation script so that rc likes it better
- add clean stanza

* Mon Oct  4 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- backed out ncurses and makeshlib patches
- update for krb5-1.1
- add KDC rotation to rc.boot, based on ideas from Michael's C version

* Mon Sep 26 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- added -lncurses to telnet and telnetd makefiles

* Mon Jul  5 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- added krb5.csh and krb5.sh to /etc/profile.d

* Mon Jun 22 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- broke out configuration files

* Mon Jun 14 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- fixed server package so that it works now

* Sat May 15 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- started changelog
- updated existing 1.0.5 RPM from Eos Linux to krb5 1.0.6
- added --force to makeinfo commands to skip errors during build

%prep
%setup -q
%patch0  -p0 -b .db
%patch1  -p0 -b .tciogltc
%patch2  -p0 -b .libpty
%patch3  -p0 -b .fixinfo
%patch4  -p0 -b .manpages
%patch5  -p0 -b .netkitr
%patch6  -p1 -b .rlogind
%patch7  -p1 -b .ksu
%patch8 -p1 -b .ksu-options
%patch9 -p1 -b .ksu-man
%patch10 -p1 -b .quiet
%patch11 -p1 -b .brokenrev
%patch12 -p1 -b .spelling
%patch13 -p1 -b .term
%patch14 -p1 -b .passive
%patch15 -p1 -b .forward
%patch16 -p1 -b .heap
%patch17 -p1 -b .wragg
%patch18 -p1 -b .statglue
cp $RPM_SOURCE_DIR/statglue.c src/util/profile/statglue.c
find . -type f -name "*.fixinfo" -exec rm -fv "{}" ";"
gzip doc/*.ps

%build
cd src
libtoolize --copy --force
cp config.{guess,sub} config/

# Can't use %%configure because we don't use the default mandir.
LDCOMBINE_TAIL="-lc"; export LDCOMBINE_TAIL
./configure \
	--with-cc=%{__cc} \
	--with-ccopts="$RPM_OPT_FLAGS -fPIC" \
	--enable-shared --enable-static \
	--prefix=%{prefix} \
	--infodir=%{_infodir} \
	--localstatedir=%{_var}/kerberos \
	--with-krb4 \
	--enable-dns --enable-dns-for-kdc --enable-dns-for-realm \
	--with-netlib=-lresolv \
	--with-tcl=%{_prefix} \
	%{_target_platform}
make

# Run the test suite.  Won't run in the build system because /dev/pts is
# not available for telnet tests and so on.
# make check TMPDIR=%{_tmppath}

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# Our shell scripts.
mkdir -p $RPM_BUILD_ROOT%{prefix}/bin
install -m 755 $RPM_SOURCE_DIR/{krsh,krlogin} $RPM_BUILD_ROOT/%{prefix}/bin/

# Extra headers.
mkdir -p $RPM_BUILD_ROOT%{prefix}/include
(cd src/include
 find kadm5 krb5 gssrpc gssapi -name "*.h" | \
 cpio -pdm  $RPM_BUILD_ROOT/%{prefix}/include )
sed 's^k5-int^krb5/kdb^g' < $RPM_BUILD_ROOT/%{prefix}/include/kadm5/admin.h \
			  > $RPM_BUILD_ROOT/%{prefix}/include/kadm5/admin.h2 &&\
mv $RPM_BUILD_ROOT/%{prefix}/include/kadm5/admin.h2 \
   $RPM_BUILD_ROOT/%{prefix}/include/kadm5/admin.h
find $RPM_BUILD_ROOT/%{prefix}/include -type d | xargs chmod 755
find $RPM_BUILD_ROOT/%{prefix}/include -type f | xargs chmod 644

# Info docs.
mkdir -p $RPM_BUILD_ROOT%{_infodir}
install -m 644 doc/*.info* $RPM_BUILD_ROOT%{_infodir}/
gzip $RPM_BUILD_ROOT%{_infodir}/*.info*

# KDC config files.
mkdir -p $RPM_BUILD_ROOT%{_var}/kerberos/krb5kdc
install -m 644 $RPM_SOURCE_DIR/kdc.conf  $RPM_BUILD_ROOT%{_var}/kerberos/krb5kdc/
install -m 644 $RPM_SOURCE_DIR/kadm5.acl $RPM_BUILD_ROOT%{_var}/kerberos/krb5kdc/

# Client config files and scripts.
mkdir -p $RPM_BUILD_ROOT/etc/profile.d
install -m 644 $RPM_SOURCE_DIR/krb5.conf $RPM_BUILD_ROOT/etc/krb5.conf
install -m 755 $RPM_SOURCE_DIR/krb5.{sh,csh} $RPM_BUILD_ROOT/etc/profile.d/

# KDC init script.
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 755 $RPM_SOURCE_DIR/krb5kdc.init $RPM_BUILD_ROOT/etc/rc.d/init.d/krb5kdc
install -m 755 $RPM_SOURCE_DIR/kadmind.init $RPM_BUILD_ROOT/etc/rc.d/init.d/kadmin
install -m 755 $RPM_SOURCE_DIR/kpropd.init $RPM_BUILD_ROOT/etc/rc.d/init.d/kprop
install -m 755 $RPM_SOURCE_DIR/krb524d.init $RPM_BUILD_ROOT/etc/rc.d/init.d/krb524
install -m 755 $RPM_SOURCE_DIR/kdcrotate $RPM_BUILD_ROOT/etc/rc.d/init.d/

# The rest of the binaries and libraries and docs.
cd src
make prefix=$RPM_BUILD_ROOT%{prefix} \
	localstatedir=$RPM_BUILD_ROOT%{_var}/kerberos \
	infodir=$RPM_BUILD_ROOT%{_infodir} install

# Fixup strange shared library permissions.
chmod 755 $RPM_BUILD_ROOT%{prefix}/lib/*.so*

# Xinetd configuration files.
mkdir -p $RPM_BUILD_ROOT/etc/xinetd.d/
for xinetd in eklogin klogin kshell krb5-telnet gssftp ; do
	install -m 644 $RPM_SOURCE_DIR/${xinetd}.xinetd \
	$RPM_BUILD_ROOT/etc/xinetd.d/${xinetd}
done

# Trim off useless info.
strip $RPM_BUILD_ROOT%{prefix}/bin/* $RPM_BUILD_ROOT%{prefix}/sbin/* || :
strip -g $RPM_BUILD_ROOT%{prefix}/lib/lib* || :

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post libs
grep -q %{prefix}/lib /etc/ld.so.conf 2> /dev/null || echo %{prefix}/lib >> /etc/ld.so.conf
/sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post server
# Remove the init script for older servers.
[ -x /etc/rc.d/init.d/krb5server ] && /sbin/chkconfig --del krb5server
# Install the new ones.
/sbin/chkconfig --add krb5kdc
/sbin/chkconfig --add kadmin
/sbin/chkconfig --add krb524
/sbin/chkconfig --add kprop
# Install info pages.
/sbin/install-info %{_infodir}/krb425.info.gz %{_infodir}/dir
/sbin/install-info %{_infodir}/krb5-admin.info.gz %{_infodir}/dir
/sbin/install-info %{_infodir}/krb5-install.info.gz %{_infodir}/dir

%preun server
if [ "$1" = "0" ] ; then
	/sbin/chkconfig --del krb5kdc
	/sbin/chkconfig --del kadmin
	/sbin/chkconfig --del krb524
	/sbin/chkconfig --del kprop
	/sbin/service krb5kdc stop > /dev/null 2>&1 || :
	/sbin/service kadmin stop > /dev/null 2>&1 || :
	/sbin/service krb524 stop > /dev/null 2>&1 || :
	/sbin/service kprop stop > /dev/null 2>&1 || :
	/sbin/install-info --delete %{_infodir}/krb425.info.gz %{_infodir}/dir
	/sbin/install-info --delete %{_infodir}/krb5-admin.info.gz %{_infodir}/dir
	/sbin/install-info --delete %{_infodir}/krb5-install.info.gz %{_infodir}/dir
fi

%postun server
if [ "$1" -ge 1 ] ; then
	/sbin/service krb5kdc condrestart > /dev/null 2>&1 || :
	/sbin/service kadmin condrestart > /dev/null 2>&1 || :
	/sbin/service krb524 condrestart > /dev/null 2>&1 || :
	/sbin/service kprop condrestart > /dev/null 2>&1 || :
fi

%post workstation
/sbin/install-info %{_infodir}/krb5-user.info %{_infodir}/dir
/sbin/service xinetd reload > /dev/null 2>&1 || :

%preun workstation
if [ "$1" = "0" ] ; then
	/sbin/install-info --delete %{_infodir}/krb5-user.info %{_infodir}/dir
fi

%postun workstation
/sbin/service xinetd reload > /dev/null 2>&1 || :

%files workstation
%defattr(-,root,root)

%config /etc/profile.d/krb5.sh
%config /etc/profile.d/krb5.csh

%config(noreplace) /etc/xinetd.d/*

%doc doc/user*.html doc/user*.ps.gz src/config-files/services.append
%attr(0755,root,root) %doc src/config-files/convert-config-files
%{_infodir}/krb5-user.info*

%dir %{prefix}
%dir %{prefix}/bin
%dir %{prefix}/man
%dir %{prefix}/man/man1
%dir %{prefix}/man/man5
%dir %{prefix}/man/man8
%dir %{prefix}/sbin

%{prefix}/bin/ftp
%{prefix}/man/man1/ftp.1*
%{prefix}/bin/gss-client
%{prefix}/bin/kdestroy
%{prefix}/man/man1/kdestroy.1*
%{prefix}/man/man1/kerberos.1*
%{prefix}/bin/kinit
%{prefix}/man/man1/kinit.1*
%{prefix}/bin/klist
%{prefix}/man/man1/klist.1*
%{prefix}/bin/kpasswd
%{prefix}/man/man1/kpasswd.1*
%{prefix}/bin/krb524init
%{prefix}/sbin/kadmin
%{prefix}/man/man8/kadmin.8*
%{prefix}/sbin/ktutil
%{prefix}/man/man8/ktutil.8*
%attr(0755,root,root) %{prefix}/bin/ksu
%{prefix}/man/man1/ksu.1*
%{prefix}/bin/kvno
%{prefix}/man/man1/kvno.1*
%{prefix}/bin/rcp
%{prefix}/man/man1/rcp.1*
%{prefix}/bin/krlogin
%{prefix}/bin/rlogin
%{prefix}/man/man1/rlogin.1*
%{prefix}/bin/krsh
%{prefix}/bin/rsh
%{prefix}/man/man1/rsh.1*
%{prefix}/bin/telnet
%{prefix}/man/man1/telnet.1*
%{prefix}/man/man1/tmac.doc*
%attr(0755,root,root) %{prefix}/bin/v4rcp
%{prefix}/man/man1/v4rcp.1*
%{prefix}/bin/v5passwd
%{prefix}/man/man1/v5passwd.1*
%{prefix}/bin/sim_client
%{prefix}/bin/uuclient
%{prefix}/sbin/login.krb5
%{prefix}/man/man8/login.krb5.8*
%{prefix}/sbin/ftpd
%{prefix}/man/man8/ftpd.8*
%{prefix}/sbin/gss-server
%{prefix}/sbin/klogind
%{prefix}/man/man8/klogind.8*
%{prefix}/sbin/krb5-send-pr
%{prefix}/man/man1/krb5-send-pr.1*
%{prefix}/sbin/kshd
%{prefix}/man/man8/kshd.8*
%{prefix}/sbin/telnetd
%{prefix}/man/man8/telnetd.8*
%{prefix}/sbin/uuserver
%{prefix}/man/man5/.k5login.5*
%{prefix}/man/man5/krb5.conf.5*

%files server
%defattr(-,root,root)

%config /etc/rc.d/init.d/krb5kdc
%config /etc/rc.d/init.d/kadmin
%config /etc/rc.d/init.d/krb524
%config /etc/rc.d/init.d/kprop

%doc doc/admin*.ps.gz doc/admin*.html
%doc doc/krb425*.ps.gz doc/krb425*.html
%doc doc/install*.ps.gz doc/install*.html

%{_infodir}/krb5-admin.info*
%{_infodir}/krb5-install.info*
%{_infodir}/krb425.info*

%dir %{_var}/kerberos
%dir %{_var}/kerberos/krb5kdc
%config(noreplace) %{_var}/kerberos/krb5kdc/kdc.conf
%config(noreplace) %{_var}/kerberos/krb5kdc/kadm5.acl

%dir %{prefix}/bin
%dir %{prefix}/man
%dir %{prefix}/man/man1
%dir %{prefix}/man/man5
%dir %{prefix}/man/man8
%dir %{prefix}/sbin

%{prefix}/man/man5/kdc.conf.5*
%{prefix}/sbin/kadmin.local
%{prefix}/man/man8/kadmin.local.8*
%{prefix}/sbin/kadmind
%{prefix}/man/man8/kadmind.8*
%{prefix}/sbin/kadmind4
%{prefix}/sbin/kdb5_util
%{prefix}/man/man8/kdb5_util.8*
%{prefix}/sbin/kprop
%{prefix}/man/man8/kprop.8*
%{prefix}/sbin/kpropd
%{prefix}/man/man8/kpropd.8*
%{prefix}/sbin/krb524d
%{prefix}/sbin/krb5kdc
%{prefix}/man/man8/krb5kdc.8*
%{prefix}/sbin/sim_server
%{prefix}/sbin/v5passwdd
# This is here for people who want to test their server, and also 
# included in devel package for similar reasons.
%{prefix}/bin/sclient
%{prefix}/man/man1/sclient.1*
%{prefix}/sbin/sserver
%{prefix}/man/man8/sserver.8*

%files libs
%defattr(-,root,root)
%config /etc/rc.d/init.d/kdcrotate
%config(noreplace) /etc/krb5.conf
%dir %{prefix}
%dir %{prefix}/lib
%{prefix}/lib/lib*.so.*.*
%{prefix}/share

%files devel
%defattr(-,root,root)
%doc doc/api
%doc doc/implement
%doc doc/kadm5
%doc doc/kadmin
%doc doc/krb5-protocol
%doc doc/rpc
%{prefix}/include

%dir %{prefix}
%dir %{prefix}/bin
%dir %{prefix}/lib
%dir %{prefix}/man
%dir %{prefix}/man/man1
%dir %{prefix}/man/man8
%dir %{prefix}/sbin

%{prefix}/lib/lib*.a
%{prefix}/lib/lib*.so

%{prefix}/bin/sclient
%{prefix}/man/man1/sclient.1*
%{prefix}/man/man8/sserver.8*
%{prefix}/sbin/sserver
