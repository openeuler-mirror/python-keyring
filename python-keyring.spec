%global _empty_manifest_terminate_build 0
Name:           python-keyring
Version:        23.0.0
Release:        1
Summary:        Store and access your passwords safely.
License:        MIT License
URL:            https://github.com/jaraco/keyring
Source0:        https://files.pythonhosted.org/packages/source/k/keyring/keyring-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-toml
Requires:       python3-importlib-metadata
Requires:       python3-SecretStorage
Requires:       python3-jeepney
Requires:       python3-pywin32-ctypes
Requires:       python3-sphinx
Requires:       python3-pytest
Requires:       python3-pytest-checkdocs
Requires:       python3-pytest-flake8
Requires:       python3-pytest-cov
Requires:       python3-pytest-black
Requires:       python3-pytest-mypy

%description
On Linux, the KWallet backend relies on dbus-python_, which does not always
install correctly when using pip (compilation is needed). For best results,
install dbus-python as a system package.

%package -n python3-keyring
Summary:	Store and access your passwords safely.
Provides:	python-keyring
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:  python3-pip

%description -n python3-keyring
On Linux, the KWallet backend relies on dbus-python_, which does not always
install correctly when using pip (compilation is needed). For best results,
install dbus-python as a system package.

%package help
Summary:	Development documents and examples for keyring
Provides:	python3-keyring-doc
%description help
On Linux, the KWallet backend relies on dbus-python_, which does not always
install correctly when using pip (compilation is needed). For best results,
install dbus-python as a system package.

%prep
%autosetup -n keyring-%{version}

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .


%files -n python3-keyring -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_pkgdocdir}

%changelog
* Wed Jul 14 2021 huangtianhua <huangtianhua@huawei.com> - 23.0.0-1
- Upgrade to 23.0.0 to support OpenStack-W

* Thu 03 2020 baizhonggui <baizhonggui@huawei.com> - 21.5.0-1
- Update to 21.5.0

* Mon Aug 10 2020 lingsheng <lingsheng@huawei.com> - 13.2.1-5
- Remove python2-keyring subpackage

* Thu Nov 28 2019 wutao <wutao61@huawei.com> - 13.2.1-4
- Package init

