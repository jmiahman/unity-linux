Summary:	Bullet - collision detection and rigid body dynamics library
Name:		bullet
Version:	2.83.6
Release:	1
License:	Zlib (BSD-like)
Group:		Libraries
Source0:	https://github.com/bulletphysics/bullet3/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-musl.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-format.patch
URL:		http://bulletphysics.org/wordpress/
#BuildRequires:	libopencl-devel
BuildRequires:	mesa-libgl-devel
BuildRequires:	opengl-glu-devel
BuildRequires:	opengl-glut-devel
BuildRequires:	cmake 
BuildRequires:	libstdc++-devel
BuildRequires:	rpm-build 

%description
Bullet is a collision detection and rigid nody dynamics library.

%package devel
Summary:	Header files for bullet libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
#Requires:	opencl-devel
Requires:	opengl-devel
Requires:	opengl-glu-devel
Requires:	opengl-glut-devel

%description devel
Header files for bullet libraries.

%package doc
Summary:	Bullet libraries documentation
Group:		Documentation

%description doc
Bullet libraries documentation.

%prep
%setup -q -n bullet3-%{version}
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
#export CXXFLAGS="-O2 -DNDEBUG -fPIC"
install -d pkgbuild
cd pkgbuild
%cmake \
	-DBUILD_SHARED_LIBS=1 \
	-DBUILD_DEMOS=0 \
	-DBUILD_MULTITHREADING=1 \
	-DBUILD_EXTRAS=1 \
	-DINSTLAL_LIBS=1 \
	-DINSTALL_EXTRA_LIBS=1 \
	-DINCLUDE_INSTALL_DIR:PATH=%{_includedir}/ \
..

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
%{_includedir}/
%{_libdir}/cmake/bullet
%{_libdir}/pkgconfig/bullet.pc

%files doc
%defattr(644,root,root,755)
%doc docs/{BulletQuickstart,Bullet_User_Manual,GPU_rigidbody_using_OpenCL}.pdf

%changelog
