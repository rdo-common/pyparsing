%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pyparsing
Version:        1.3
Release:        1
Summary:        An object-oriented approach to text processing

Group:          Development/Libraries
License:        MIT
URL:            http://pyparsing.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/pyparsing/pyparsing-1.3.tar.gz
Source1:        pyparsing-LICENSE
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  %{__python}

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
%doc CHANGES examples HowToUsePyparsing.html htmldoc pyparsingClassDiagram.png README LICENSE
%{python_sitelib}/pyparsing.py
%{python_sitelib}/pyparsing.py[co]

%changelog
* Wed Aug  3 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.3-1
- Initial RPM release
