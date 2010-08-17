#
# Conditional build:
#
%define		qtver		4.6.3
%define		kdever		4.5.0

Summary:	libktorrent
Summary(pl.UTF-8):	libktorrent
Name:		libktorrent
Version:	1.0.2
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://ktorrent.org/downloads/4.0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	1d2a056de32db4c9e3224eac517f26bd
URL:		http://ktorrent.org/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ktorrent library.

%description -l pl.UTF-8
Biblioteka ktorrent.

%package devel
Summary:        Header files for ktorrent library
Summary(pl.UTF-8):      Pliki nagłówkowe biblioteki ktorrent
Group:          Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description devel
Header files for ktorrent library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ktorrent.

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

# remove unsupported langs
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/sr@ijekavian*

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libktorrent.so.?
%attr(755,root,root) %{_libdir}/libktorrent.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libktorrent.so
%{_includedir}/libktorrent
%{_datadir}/apps/cmake/modules/FindKTorrent.cmake
