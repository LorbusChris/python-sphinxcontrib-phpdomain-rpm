# Created by pyp2rpm-3.3.2
%global pypi_name sphinxcontrib-phpdomain

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        3%{?dist}
Summary:        Sphinx extension to enable documenting PHP code

License:        BSD
URL:            https://github.com/markstory/sphinxcontrib-phpdomain
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This package contains the phpdomain Sphinx extension.This extension provides a
PHP domain for sphinx

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:      (python2dist(sphinx) >= 1.3 with python2dist(sphinx) < 2.0)

%description -n python2-%{pypi_name}
This package contains the phpdomain Sphinx extension.This extension provides a
PHP domain for sphinx

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:      (python3dist(sphinx) >= 1.3 with python3dist(sphinx) < 2.0)

%description -n python3-%{pypi_name}
This package contains the phpdomain Sphinx extension.This extension provides a
PHP domain for sphinx


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/sphinxcontrib
%{python2_sitelib}/sphinxcontrib_phpdomain-%{version}-py?.?-*.pth
%{python2_sitelib}/sphinxcontrib_phpdomain-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/sphinxcontrib_phpdomain-%{version}-py?.?-*.pth
%{python3_sitelib}/sphinxcontrib_phpdomain-%{version}-py?.?.egg-info

%changelog
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.7

* Tue Jun 26 2018 Christian Glombek <lorbus@fedoraproject.org> - 0.4.1-1
- Initial package.
