Name:		i2p-plugin-neodatis
# Version from plugin.config (shortened)
Version:	2.1
Release:	1%{?dist}
Summary:	NeoDatis object database plugin for I2P	

Group:		Applications/Internet
# License from plugin.config (WTFPL) and from neodatis.org (LGPL)
License:	LGPL and WTFPL
URL:		http://sponge.i2p/files/seedless/01_neodatis.xpi2p
# FIXTHIS: This is a the binary in a archive folder
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


%install
rm -rf $RPM_BUILD_ROOT
# Install to i2p plugins (-p, --preserve-timestamps for extra security)
install -d -p -m700 $RPM_BUILD_ROOT/usr/local/i2p/.i2p/plugins
# FIXTHIS: Use install, not cp
cp -R 01_neodatis $RPM_BUILD_ROOT/usr/local/i2p/.i2p/plugins/


%post
# Condrestart i2p and return 0
/sbin/service i2p condrestart >/dev/null 2>&1 || :
# Set owner and group to i2p
chown i2p:i2p -R /usr/local/i2p/.i2p


%postun
# Condrestart i2p and return 0
/sbin/service i2p condrestart >/dev/null 2>&1 || :


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/usr/local/i2p/.i2p/plugins/01_neodatis


%changelog
* Sat Mar 24 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.1-1
- Initial package
