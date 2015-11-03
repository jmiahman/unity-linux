Summary:	Bullet - collision detection and rigid body dynamics library
Summary(pl.UTF-8):	Bullet - biblioteka wykrywania kolizji oraz dynamiki ciała sztywnego
Name:		bullet
Version:	2.83.6
Release:	1
License:	Zlib (BSD-like)
Group:		Libraries
#Source0Download: https://github.com/bulletphysics/bullet3/releases
Source0:	https://github.com/bulletphysics/bullet3/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	44cb2464336a2082b2c144194c2a2668
Patch0:		%{name}-link.patch
Patch1:		%{name}-format.patch
URL:		http://bulletphysics.org/wordpress/
BuildRequires:	libopencl-devel
BuildRequires:	libgl-devel >= 3.0
BuildRequires:	opengl-glu-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bullet is a collision detection and rigid nody dynamics library.

%description -l pl.UTF-8
Bullet to biblioteka wykrywania kolizji oraz dynamiki ciała sztywnego.

%package devel
Summary:	Header files for bullet libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek bullet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenCL-devel
Requires:	OpenGL-devel >= 3.0
Requires:	OpenGL-GLU-devel
Requires:	OpenGL-glut-devel

%description devel
Header files for bullet libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek bullet.

%package doc
Summary:	Bullet libraries documentation
Summary(pl.UTF-8):	Dokumentacja do bibliotek bullet
Group:		Documentation

%description doc
Bullet libraries documentation.

%description doc -l pl.UTF-8
Dokumentacja do bibliotek bullet.

%prep
%setup -q -n bullet3-%{version}
%patch0 -p1
%patch1 -p1

%build
install -d pkgbuild
cd pkgbuild
%cmake .. \
	-DBUILD_CPU_DEMOS=OFF \
	-DBUILD_EXTRAS=ON \
	-DBUILD_OPENGL3_DEMOS=OFF \
	-DINSTALL_EXTRA_LIBS=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C pkgbuild install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt LICENSE.txt README.md
%attr(755,root,root) %{_libdir}/libBullet2FileLoader.so.*.*
%attr(755,root,root) %{_libdir}/libBullet3Collision.so.*.*
%attr(755,root,root) %{_libdir}/libBullet3Common.so.*.*
%attr(755,root,root) %{_libdir}/libBullet3Dynamics.so.*.*
%attr(755,root,root) %{_libdir}/libBullet3Geometry.so.*.*
%attr(755,root,root) %{_libdir}/libBullet3OpenCL_clew.so.*.*
%attr(755,root,root) %{_libdir}/libBulletCollision.so.*.*
%attr(755,root,root) %{_libdir}/libBulletDynamics.so.*.*
%attr(755,root,root) %{_libdir}/libBulletFileLoader.so.*.*
%attr(755,root,root) %{_libdir}/libBulletSoftBody.so.*.*
%attr(755,root,root) %{_libdir}/libBulletWorldImporter.so.*.*
%attr(755,root,root) %{_libdir}/libBulletXmlWorldImporter.so.*.*
%attr(755,root,root) %{_libdir}/libConvexDecomposition.so.*.*
%attr(755,root,root) %{_libdir}/libGIMPACTUtils.so.*.*
%attr(755,root,root) %{_libdir}/libHACD.so.*.*
%attr(755,root,root) %{_libdir}/libLinearMath.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libBullet2FileLoader.so
%attr(755,root,root) %{_libdir}/libBullet3Collision.so
%attr(755,root,root) %{_libdir}/libBullet3Common.so
%attr(755,root,root) %{_libdir}/libBullet3Dynamics.so
%attr(755,root,root) %{_libdir}/libBullet3Geometry.so
%attr(755,root,root) %{_libdir}/libBullet3OpenCL_clew.so
%attr(755,root,root) %{_libdir}/libBulletCollision.so
%attr(755,root,root) %{_libdir}/libBulletDynamics.so
%attr(755,root,root) %{_libdir}/libBulletFileLoader.so
%attr(755,root,root) %{_libdir}/libBulletSoftBody.so
%attr(755,root,root) %{_libdir}/libBulletWorldImporter.so
%attr(755,root,root) %{_libdir}/libBulletXmlWorldImporter.so
%attr(755,root,root) %{_libdir}/libConvexDecomposition.so
%attr(755,root,root) %{_libdir}/libGIMPACTUtils.so
%attr(755,root,root) %{_libdir}/libHACD.so
%attr(755,root,root) %{_libdir}/libLinearMath.so
%{_includedir}/bullet
%{_libdir}/cmake/bullet
%{_pkgconfigdir}/bullet.pc

%files doc
%defattr(644,root,root,755)
%doc docs/{BulletQuickstart,Bullet_User_Manual,GPU_rigidbody_using_OpenCL}.pdf
