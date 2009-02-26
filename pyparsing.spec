%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pyparsing
Version:        1.5.0
Release:        4%{?dist}
Summary:        An object-oriented approach to text processing

Group:          Development/Libraries
License:        MIT
URL:            http://pyparsing.wikispaces.com/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        pyparsing-LICENSE
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel

%description
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.

%prep
%setup -q

%build
%{__python} setup.py build
mv pyparsingClassDiagram.PNG pyparsingClassDiagram.png
install -p -m 0644 %{SOURCE1} $RPM_BUILD_DIR/%{name}-%{version}/LICENSE

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES docs examples HowToUsePyparsing.html htmldoc pyparsingClassDiagram.* README LICENSE
%if 0%{?fedora} >= 9
%{python_sitelib}/pyparsing*egg-info
%endif
%{python_sitelib}/pyparsing.py*


%changelog
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.5.0-3
- Rebuild for Python 2.6

* Mon Aug  4 2008 José Matos <jamatos[AT]fc.up.pt> - 1.5.0-2
- respun (now with the right sources)

* Mon Aug  4 2008 José Matos <jamatos[AT]fc.up.pt> - 1.5.0-1
- new upstream release.

* Tue Apr  1 2008 José Matos <jamatos[AT]fc.up.pt> - 1.4.11-1
- New upstream version, add egg-info for F9+.

* Wed Aug 29 2007 José Matos <jamatos[AT]fc.up.pt> - 1.4.7-1
- New upstream version.

* Sat Apr 21 2007 José Matos <jamatos[AT]fc.up.pt> - 1.4.6-1
- New upstream version.

* Mon Dec 11 2006 José Matos <jamatos[AT]fc.up.pt> - 1.4.4-1
- New upstream version.

* Mon Sep 11 2006 José Matos <jamatos[AT]fc.up.pt> - 1.4.3-1
- New version.

* Wed Aug  3 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.3-1
- Initial RPM release
