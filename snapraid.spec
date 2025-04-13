Name:           snapraid
Summary:        Disk array backup for many large rarely-changed files
Version:        12.4
Release:        3%{?dist}
License:        GPLv3+
Group:          Applications/System
URL:            http://www.snapraid.it/
Source0:        https://github.com/amadvance/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
#BuildRequires:  gcc
#BuildRequires:  make
#BuildRequires:  libblkid-devel


%patchlist
autoreconf.patch
autoupdate.patch

%description
SnapRAID is a backup program for disk arrays. It stores parity
information of your data and it's able to recover from up to six disk
failures. SnapRAID is mainly targeted for a home media center, with a
lot of big files that rarely change.

%prep
#%setup -q
%autosetup

%build
%configure
#make %{?_smp_mflags}
%make_build

%check
make check

%install
#make install DESTDIR=%{buildroot}
make_install DESTDIR=%{buildroot}


%files
%doc COPYING AUTHORS HISTORY README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
