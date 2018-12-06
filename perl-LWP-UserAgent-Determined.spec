#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-LWP-UserAgent-Determined
Version  : 1.07
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/LWP-UserAgent-Determined-1.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/LWP-UserAgent-Determined-1.07.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblwp-useragent-determined-perl/liblwp-useragent-determined-perl_1.07-1.debian.tar.xz
Summary  : 'a virtual browser that retries errors'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-LWP-UserAgent-Determined-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(LWP)
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)

%description
Time-stamp: "2004-04-08 22:37:47 ADT"
NAME
LWP::UserAgent::Determined - a virtual browser that retries errors

%package dev
Summary: dev components for the perl-LWP-UserAgent-Determined package.
Group: Development
Provides: perl-LWP-UserAgent-Determined-devel = %{version}-%{release}

%description dev
dev components for the perl-LWP-UserAgent-Determined package.


%package license
Summary: license components for the perl-LWP-UserAgent-Determined package.
Group: Default

%description license
license components for the perl-LWP-UserAgent-Determined package.


%prep
%setup -q -n LWP-UserAgent-Determined-1.07
cd ..
%setup -q -T -D -n LWP-UserAgent-Determined-1.07 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/LWP-UserAgent-Determined-1.07/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-LWP-UserAgent-Determined
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-LWP-UserAgent-Determined/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/LWP/UserAgent/Determined.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/LWP::UserAgent::Determined.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-LWP-UserAgent-Determined/deblicense_copyright
