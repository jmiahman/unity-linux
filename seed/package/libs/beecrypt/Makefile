#
# Copyright (C) 2006-2010 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=beecrypt
PKG_VERSION:=4.2.1
PKG_RELEASE:=1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=http://pkgs.fedoraproject.org/repo/pkgs/beecrypt/beecrypt-4.2.1.tar.gz/8441c014170823f2dff97e33df55af1e/
PKG_MD5SUM:=
PKG_LICENSE:=GPL

PKG_FIXUP:=autoreconf
PKG_REMOVE_FILES:=autogen.sh aclocal.m4

PKG_INSTALL:=1
PKG_BUILD_PARALLEL:=1

DEPENDS:=+libpthread +libstdc++

include $(INCLUDE_DIR)/package.mk

TARGET_CFLAGS += $(FPIC)

define Package/libbeecrypt
  SECTION:=libs
  CATEGORY:=Libraries
  TITLE:=BeeCrypt is an ongoing project to provide a strong and fast cryptography toolkit.
  URL:=http://beecrypt.sourceforge.net/
  DEPENDS:=+libpthread +libstdcpp
endef

define Build/Configure
	$(call Build/Configure/Default, \
        --disable-expert-mode \
        --without-java \
        --without-python \
        --disable-openmp \
	--without-cplusplus \
	)
endef

define Build/InstallDev
	$(INSTALL_DIR) $(1)/usr/include
	$(CP) $(PKG_INSTALL_DIR)/usr/include/* $(1)/usr/include/
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/* $(1)/usr/lib/
endef

define Package/libbeecrypt/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(CP) $(PKG_INSTALL_DIR)/usr/lib/* $(1)/usr/lib/
endef

$(eval $(call RequireCommand,xgettext, \
	$(PKG_NAME) requires the GNU gettext development package installed on the local system to build. \
))

$(eval $(call BuildPackage,libbeecrypt))

