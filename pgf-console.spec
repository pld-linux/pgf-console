Summary:	PGF (Progressive Graphics File) console application
Summary(pl.UTF-8):	Aplikacja terminalowa do obsługi plików PGF (Progressive Graphics File)
Name:		pgf-console
Version:	6.14.12
Release:	2
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/libpgf/%{name}-src-%{version}.tar.gz
# Source0-md5:	7c6a42ac0555d1125ba3af5161c5a777
Patch0:		pgf-lfs.patch
URL:		http://www.libpgf.org/
# FreeImage and FreeImagePlus
BuildRequires:	FreeImage-devel >= 3.16.0-1
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libpgf-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pgf is a console application for working with PGF (Progressive
Graphics File) images.

%description -l pl.UTF-8
pgf to aplikacja terminalowa do pracy z plikami obrazów PGF
(Progressive Graphics File).

%prep
%setup -q -n pgf
%undos configure.ac
%patch0 -p1

# disable doxygen docs, useless for program package
%{__sed} -i -e '/^SUBDIRS/s/ doc//' Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# nonsense
%{__rm} -r $RPM_BUILD_ROOT%{_bindir}/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog FAQ README
%attr(755,root,root) %{_bindir}/pgf
