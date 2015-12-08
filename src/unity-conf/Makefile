VERSION		:= 0.0.5

sysconfdir      ?= /etc/lbu

PREFIX		?= /usr

M_ARCH := $(shell uname -m)

ifeq (x86_64,${M_ARCH})
LIBDIR ?= $(PREFIX)/lib64
else
LIBDIR ?= $(PREFIX)/lib
endif

LIB_FILES	:= libunity.sh
SBIN_FILES	:= lbu\
		setup-acf\
		setup-unity\
		setup-apkcache\
		setup-apkrepos\
		setup-bootable\
		setup-disk\
		setup-dns\
		setup-gparted-desktop\
		setup-hostname\
		setup-interfaces\
		setup-keymap\
		setup-lbu\
		setup-mta\
		setup-ntp\
		setup-proxy\
		setup-sshd\
		setup-timezone\
		setup-xen-dom0\
		setup-xorg-base\
		update-conf\
		update-kernel

BIN_FILES	:= uniso

SCRIPTS		:= $(LIB_FILES) $(SBIN_FILES)

ETC_LBU_FILES	:= lbu.conf

GIT_REV		:= $(shell test -d .git && git describe || echo exported)
ifneq ($(GIT_REV), exported)
FULL_VERSION    := $(patsubst $(PACKAGE)-%,%,$(GIT_REV))
FULL_VERSION    := $(patsubst v%,%,$(FULL_VERSION))
else
FULL_VERSION    := $(VERSION)
endif


DESC="Unity configuration scripts"
WWW="http://unitylinux.org/unity-conf"


SED		:= sed

SED_REPLACE	:= -e 's:@VERSION@:$(FULL_VERSION):g' \
			-e 's:@PREFIX@:$(PREFIX):g' \
			-e 's:@sysconfdir@:$(sysconfdir):g'

.SUFFIXES:	.sh.in .in
%.sh: %.sh.in
	${SED} ${SED_REPLACE} ${SED_EXTRA} $< > $@

%: %.in
	${SED} ${SED_REPLACE} ${SED_EXTRA} $< > $@

.PHONY:	all apk clean install uninstall
all:	$(SCRIPTS) $(BIN_FILES)

uniso:	uniso.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^

apk:	$(APKF)

install: $(BIN_FILES) $(SBIN_FILES) $(LIB_FILES) $(ETC_LBU_FILES)
	install -m 755 -d $(DESTDIR)/$(PREFIX)/bin
	install -m 755 $(BIN_FILES) $(DESTDIR)$(PREFIX)/bin
	install -m 755 -d $(DESTDIR)/$(PREFIX)/sbin
	install -m 755 $(SBIN_FILES) $(DESTDIR)/$(PREFIX)/sbin
	install -m 755 -d $(DESTDIR)/$(LIBDIR)
	install -m 755 $(LIB_FILES) $(DESTDIR)/$(LIBDIR)
	install -m 755 -d $(DESTDIR)/$(sysconfdir)
	install -m 755 $(ETC_LBU_FILES) $(DESTDIR)/$(sysconfdir)

uninstall:
	for i in $(SBIN_FILES); do \
		rm -f "$(DESTDIR)/$(PREFIX)/sbin/$$i";\
	done
	for i in $(LIB_FILES); do \
		rm -f "$(DESTDIR)/$(LIBDIR)/$$i";\
	done

#---------------- make tar -----------------------------------------------------------------------------
TD	= $(shell basename `pwd`)
targz:
	mkdir $(TD)-$(FULL_VERSION)
	find . -name "*" -type f -exec cp -rf {} $(TD)-$(FULL_VERSION) \;
	tar --create --verbose --gzip --file $(TD)-$(FULL_VERSION).tar.gz \
	$(TD)-$(FULL_VERSION)
	rm -rf $(TD)-$(FULL_VERSION)

#-------------- end make tar ---------------------------------------------------------------------------


clean:
	rm -rf $(SCRIPTS) $(BIN_FILES)

