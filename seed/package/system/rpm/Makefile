#
# Copyright (C) 2006-2010 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=rpm
PKG_VERSION:=5.2.1
PKG_RELEASE:=1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=http://rpm5.org/files/rpm/rpm-5.2/
PKG_MD5SUM:=
PKG_LICENSE:=GPL

DEPENDS:=+libz +libssl +libpthread +libcrypto +libbeecrypt +libpopt +libdb

PKG_FIXUP:=autoreconf
PKG_REMOVE_FILES:=autogen.sh aclocal.m4

PKG_INSTALL:=1
PKG_BUILD_PARALLEL:=1

include $(INCLUDE_DIR)/package.mk

define Package/rpm
  SECTION:=base
  CATEGORY:=Base system
  TITLE:=A powerful command line driven package management system
  URL:=http://rpm5.org/
  DEPENDS:=+zlib +libopenssl +libpthread +libcrypto +libbeecrypt +libpopt +libdb47 +lua +liblua
  PKG_BUILD_DEPENDES:=libintl-full
endef

define Build/Configure
	$(call Build/Configure/Default, \
        --host=$(REAL_GNU_TARGET_NAME) \
        --build=$(GNU_HOST_NAME) \
        --target=$(REAL_GNU_TARGET_NAME) \
        --with-bugreport=JMiahMan@unity-linux.org \
        --disable-build-versionscript \
        --disable-rpath \
        --without-selinux \
        --without-python \
        --without-perl \
        --with-lua=external \
        --with-openssl=external \
        --with-db=external \
        --with-popt=$(STAGING_DIR) \
        --with-zlib=$(STAGING_DIR) \
        --with-libbeecrypt=$(STAGING_DIR) \
        --with-bzip2 \
	)
endef

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/*.{a,so*} $(1)/usr/lib/
endef

define Package/rpm/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/* $(1)/usr/lib/
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/rpm $(1)/usr/bin/
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/rpmbuild $(1)/usr/bin/
endef

$(eval $(call BuildPackage,rpm))

