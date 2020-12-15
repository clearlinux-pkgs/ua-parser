#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3B2D400CE5BBCA60 (m@robenolt.com)
#
Name     : ua-parser
Version  : 0.10.0
Release  : 16
URL      : https://files.pythonhosted.org/packages/92/68/b5c60fc7386d95de9d66a42b9a9d4898d74de895368964b198003042e297/ua-parser-0.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/92/68/b5c60fc7386d95de9d66a42b9a9d4898d74de895368964b198003042e297/ua-parser-0.10.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/92/68/b5c60fc7386d95de9d66a42b9a9d4898d74de895368964b198003042e297/ua-parser-0.10.0.tar.gz.asc
Summary  : Python port of Browserscope's user agent parser
Group    : Development/Tools
License  : Apache-2.0
Requires: ua-parser-license = %{version}-%{release}
Requires: ua-parser-python = %{version}-%{release}
Requires: ua-parser-python3 = %{version}-%{release}
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3

%description
uap-python
==========
A python implementation of the UA Parser (https://github.com/ua-parser,
formerly https://github.com/tobie/ua-parser)

%package license
Summary: license components for the ua-parser package.
Group: Default

%description license
license components for the ua-parser package.


%package python
Summary: python components for the ua-parser package.
Group: Default
Requires: ua-parser-python3 = %{version}-%{release}

%description python
python components for the ua-parser package.


%package python3
Summary: python3 components for the ua-parser package.
Group: Default
Requires: python3-core
Provides: pypi(ua_parser)

%description python3
python3 components for the ua-parser package.


%prep
%setup -q -n ua-parser-0.10.0
cd %{_builddir}/ua-parser-0.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603406957
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ua-parser
cp %{_builddir}/ua-parser-0.10.0/ua_parser/LICENSE %{buildroot}/usr/share/package-licenses/ua-parser/c0204dc0e6cdf836b06fd8a9c55fd9ff5ca60245
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ua-parser/c0204dc0e6cdf836b06fd8a9c55fd9ff5ca60245

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
