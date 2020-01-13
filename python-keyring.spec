Name:           python-keyring
Version:        13.2.1
Release:        4
Summary:        Python library to access the system keyring service
License:        MIT and Python
URL:            https://github.com/jaraco/keyring
Source0:        https://files.pythonhosted.org/packages/source/k/keyring/keyring-%{version}.tar.gz
BuildArch:      noarch

%description
The Python keyring lib provides a easy way to access the system keyring
service from python. It can be used in any application that needs safe
password storage.
This package only provides file-based pseudo-keyrings. To interface with
gnome-keyring or KWallet, please install one of python-keyring-gnome or
python-keyring-kwallet.

%package -n     python2-keyring
Summary:        A library to get keyring service by python2
BuildRequires:  python2-devel python2-setuptools python2-setuptools_scm python2-pytest-cov
BuildRequires:  python2-keyczar python2-mock
BuildRequires:  python2-entrypoints python2-pytest libffi-devel openssl-devel

Requires:       python2-SecretStorage python2-entrypoints

%{?python_provide:%python_provide python2-keyring}

Obsoletes:      %{name}-kwallet < %{version}-%{release} %{name}-gnome < %{version}-%{release}

%description -n python2-keyring
The Python keyring lib provides a easy way to access the system keyring
service from python. It can be used in any application that needs safe
password storage.

%package -n     python%{python3_pkgversion}-keyring
Summary:        A library to get keyring service by python3
BuildRequires:  python%{python3_pkgversion}-devel python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-entrypoints python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-cov

Requires:       python%{python3_pkgversion}-SecretStorage python%{python3_pkgversion}-entrypoints

%{?python_provide:%python_provide python%{python3_pkgversion}-keyring}

%description -n python%{python3_pkgversion}-keyring
The Python keyring lib provides a easy way to access the system keyring
service from python. It can be used in any application that needs safe
password storage.

%prep
%autosetup -n keyring-%{version} -p1
rm -frv keyring.egg-info
sed -i '1{\@^#!/usr/bin/env python@d}' keyring/cli.py
sed -i -e "\@use_vcs_version@s/^.*$/\tversion = \"%{version}\",/g" -e {/\'hgtools\'/d} setup.py

%build
%py2_build
%py3_build

%install
%py2_install
mv %{buildroot}%{_bindir}/keyring %{buildroot}%{_bindir}/keyring-python2
%py3_install
cp -a %{buildroot}%{_bindir}/keyring %{buildroot}%{_bindir}/keyring-python%{python3_pkgversion}


%files -n python2-keyring
%{_bindir}/keyring-python2
%{python2_sitelib}/{keyring,keyring-%{version}-py%{python2_version}.egg-info}
%doc CHANGES.rst README.rst

%files -n python%{python3_pkgversion}-keyring
%{_bindir}/{keyring-python%{python3_pkgversion},keyring}
%{python3_sitelib}/{keyring-%{version}-py%{python3_version}.egg-info,keyring}
%doc CHANGES.rst README.rst

%changelog
* Thu Nov 28 2019 wutao <wutao61@huawei.com> - 13.2.1-4
- Package init

