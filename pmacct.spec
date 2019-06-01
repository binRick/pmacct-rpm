Name:           pmacct
Version:        1.7.2
Release:        1%{?dist}
Summary:        passive network monitoring

License:        GPLv2
URL:            http://www.pmacct.net/
Source0:        http://www.pmacct.net/pmacct-%{version}.tar.gz

%define _unpackaged_files_terminate_build 0


BuildRequires:  sqlite-devel, libpcap-devel, zlib-devel, jansson-devel, mariadb-devel

%description
pmacct is a small set of multi-purpose passive network monitoring tools

%prep
%setup -q

%build
./autogen.sh
%configure --enable-sqlite3 --enable-jansson --enable-mysql --enable-geoipv2
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -type f | sed 's|^%{buildroot}||' > filelist

%files -f filelist
