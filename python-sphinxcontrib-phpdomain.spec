# Created by pyp2rpm-3.3.2
%global pypi_name sphinxcontrib-phpdomain

Name:           python-%{pypi_name}
Version:        0.6.1
Release:        3%{?dist}
Summary:        Sphinx extension to enable documenting PHP code

License:        BSD
URL:            https://github.com/markstory/sphinxcontrib-phpdomain
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This package contains the phpdomain Sphinx extension.This extension provides a
PHP domain for sphinx

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:      (python3dist(sphinx) >= 1.3 with python3dist(sphinx) < 2.2)

%description -n python3-%{pypi_name}
This package contains the phpdomain Sphinx extension.This extension provides a
PHP domain for sphinx


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/sphinxcontrib_phpdomain-%{version}-py?.?-*.pth
%{python3_sitelib}/sphinxcontrib_phpdomain-%{version}-py?.?.egg-info

%changelog
* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-2
- Rebuilt for Python 3.8

* Sun Jul 28 2019 Christian Glombek <lorbus@fedoraproject.org> - 0.6.1-1
- Update to v0.6.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.7

* Tue Jun 26 2018 Christian Glombek <lorbus@fedoraproject.org> - 0.4.1-1
- Initial package.
