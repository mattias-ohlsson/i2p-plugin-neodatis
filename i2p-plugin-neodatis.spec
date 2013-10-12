Name:		i2p-plugin-neodatis
# Version from plugin.config (2.1-2.14-209-16)
Version:	2.1
Release:	2.14.209.16.1%{?dist}
Summary:	NeoDatis object database plugin for I2P	

Group:		Applications/Internet
# License from plugin.config (WTFPL) and from neodatis.org (LGPL)
License:	LGPL and WTFPL
URL:		http://sponge.i2p/files/seedless/01_neodatis.xpi2p
# FIXTHIS: This is a binary in an archive folder
Source0:	i2p-plugin-neodatis-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	p7zip
Requires:	i2p

# Description from www.neodatis.org
%description
NeoDatis ODB is a very simple Object Database that currently runs on the Java, .Net, Google Android, Groovy and Scala. This is a plugin for I2P. 

%prep
%setup -q
# Extract the xpi package with 7zip to 01_neodatis
7za x -o01_neodatis 01_neodatis.xpi2p


%build
# This is a binary

# Disable automatic update
sed -i \
  -e 's|updateURL=|#DISABLED (rpm package): updateURL=|g' \
  01_neodatis/plugin.config


%install
rm -rf $RPM_BUILD_ROOT
# Install to i2p plugins (-p, --preserve-timestamps for extra security)
install -d -p $RPM_BUILD_ROOT/usr/local/i2p/.i2p/plugins
# FIXTHIS: Use install, not cp
cp -R 01_neodatis $RPM_BUILD_ROOT/usr/local/i2p/.i2p/plugins/


%post
# Condrestart i2p and return 0
/sbin/service i2p condrestart >/dev/null 2>&1 || :


%postun
# Condrestart i2p and return 0
/sbin/service i2p condrestart >/dev/null 2>&1 || :


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(700,i2p,i2p,700)
%doc
# list all folders to apply defattr
/usr/local/i2p/.i2p
/usr/local/i2p/.i2p/plugins
/usr/local/i2p/.i2p/plugins/01_neodatis


%changelog
* Mon Jul 9 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.1-2.14.209.16.1
- New version

* Mon Apr 9 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.1-2
- Disable automatic update

* Sat Mar 24 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.1-1
- Initial package
