Name:		testdrive-fedora
Version: 	0.1.0
Release: 	1%{?dist}
Summary: 	Skrypt do testowania Fedory na maszynie wirtualnej
 
Group: 		Applications/System
License: 	GPL
URL: 		http://godlewski.ayz.pl/
 
Source0: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
 
Requires: 	VirtualBox-OSE
Requires: 	wget
Requires: 	rsync

 
%description -l pl
Skrypt pozwalający na pobranie buildu najnowszego (niestabilnego) obrazu Fedory
z repozytorium Rawhide.
 
%prep
%setup -q
 
%build
echo -e "Nothing to build."
 
%install
 
rm -rf %{buildroot}
mkdir -p %{buildroot}
mv img/testdrive.png %{buildroot}/%{_datadir}/testdrive
mv testdrive testdrive-select-iso %{buildroot}/usr/bin

 
%clean
rm -rf %{buildroot}
 
%files
%defattr(0744,root,root,0755)
 
%changelog
* Wed Dec 30 2009 Piotr Godlewski <godlewski.piotr@gmail.com> - 0.1.0-1
- Pierwsz próba.
