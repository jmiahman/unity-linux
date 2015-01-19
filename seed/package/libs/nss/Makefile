# 
# Copyright (C) 2006-2010 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=nss
PKG_VERSION:=3.16.6
PKG_RELEASE:=1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION)-with-nspr-4.10.6.tar.gz
PKG_SOURCE_URL:=ftp://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/NSS_3_16_6_RTM/src/
PKG_MD5SUM:=
HOST_BUILD_DIR:=$(BUILD_DIR_HOST)/$(PKG_NAME)-$(PKG_VERSION)
#PKG_BUILD_DEPENDS:=nss/host

PKG_FIXUP:=libtool

MAKE_PATH:=nss

include $(INCLUDE_DIR)/package.mk
include $(INCLUDE_DIR)/host-build.mk

HOST_INCL:="-I$(HOST_BUILD_DIR)/nspr/pr/include \
	    -I$(HOST_BUILD_DIR)/nss/lib/dbm/include \
            -L${STAGING_DIR}/lib"

define Host/Compile
	$(MAKE) -C $(HOST_BUILD_DIR)/nss/coreconf
	$(MAKE) -C $(HOST_BUILD_DIR)/nss
endef

define Build/Configure
endef

define Package/libnss
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=Library Network Security Services (NSS)
  URL:=http://www.mozilla.org/projects/security/pki/nss/
endef

define Package/libnss/description
  Library Network Security Services (NSS)
endef

define Build/Configure
endef

define Build/Compile
#	(cd $(PKG_BUILD_DIR)/nss; $(MAKE) coreconf CC="$(HOSTCC)" CFLAGS="$(HOST_CFLAGS)" CPPFLAGS="$(HOST_CFLAGS)" LDFLAGS="$(HOST_LDFLAGS)")
#	(cd $(PKG_BUILD_DIR)/nss; $(MAKE) lib/dbm all CC="$(TARGET_CC)" CFLAGS="$(TARGET_CFLAGS)" CPPFLAGS="$(TARGET_CFLAGS)" LDFLAGS="$(TARGET_LDFLAGS)")
	$(MAKE) -C $(PKG_BUILD_DIR)/nss/coreconf CC="$(TARGET_CC)" CFLAGS="$(TARGET_CFLAGS)"
#	$(MAKE) -C $(PKG_BUILD_DIR)/mozilla/security/dbm CC="$(TARGET_CC)" CFLAGS="$(TARGET_CFLAGS)"
	$(MAKE) -C $(PKG_BUILD_DIR)/nss CC="$(TARGET_CC)" CFLAGS="$(TARGET_CFLAGS)"
endef

define Package/libnss/install
#	$(INSTALL_DIR) $(1)/usr/lib
#	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libnss.so* $(1)/usr/lib
endef

define Build/InstallDev
#	$(INSTALL_DIR) $(1)/usr/include
#	$(INSTALL_DIR) $(1)/usr/lib
#	$(INSTALL_DIR) $(1)/usr/lib/pkgconfig
#	$(CP) $(PKG_INSTALL_DIR)/usr/lib/libnss.{a,so*} $(1)/usr/lib
#	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include
#	$(SED) 's,/usr,${STAGING_DIR}/usr,g' $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/libnss.pc
#	$(CP) $(PKG_INSTALL_DIR)/usr/lib/pkgconfig/libnss.pc $(1)/usr/lib/pkgconfig/libnss.pc
endef

$(eval $(call BuildPackage,libnss))
#$(eval $(call HostBuild))
