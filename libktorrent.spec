#
# Conditional build:
#
%define		qtver		4.6.2
%define		kdever		4.4.4

Summary:	libktorrent
Summary(pl.UTF-8):	libktorrent
Name:		libktorrent
Version:	1.0.0
Release:	0.1
License:	GPL
Group:		X11/Libraries
Source0:	http://ktorrent.org/downloads/4.0/%{name}-%{version}.tar.bz2
# Source0-md5:
URL:		http://ktorrent.org/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libktorrent.

%description -l pl.UTF-8
libktorrent.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
