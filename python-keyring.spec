Name:           python-keyring
Version:        13.2.1
Release:        5
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
%py3_build

%install
%py3_install
cp -a %{buildroot}%{_bindir}/keyring %{buildroot}%{_bindir}/keyring-python%{python3_pkgversion}

%files -n python%{python3_pkgversion}-keyring
%{_bindir}/{keyring-python%{python3_pkgversion},keyring}
%{python3_sitelib}/{keyring-%{version}-py%{python3_version}.egg-info,keyring}
%doc CHANGES.rst README.rst

%changelog
* Mon Aug 10 2020 lingsheng <lingsheng@huawei.com> - 13.2.1-5
- Remove python2-keyring subpackage

* Thu Nov 28 2019 wutao <wutao61@huawei.com> - 13.2.1-4
- Package init

