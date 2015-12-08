#!/bin/sh

[ $# != 1 ] && exit 1

CARD=$1

. /etc/rc.d/init.d/functions
[ -f /etc/sysconfig/alsa-udev ] && . /etc/sysconfig/alsa-udev

case "$ACTION" in
    add)
	eval LOAD_MODULES="\$MODULES_$CARD"
	for i in "$LOAD_MODULES"; do
	    /sbin/modprobe -q --ignore-install $i
	done

	if is_yes "$OSS_EMULATION"; then
	    /sbin/modprobe -q --ignore-install snd_pcm_oss
	    [ -e /dev/snd/seq ] && /sbin/modprobe -q --ignore-install snd_seq_oss
	fi

	/usr/sbin/alsactl restore "$CARD"

	eval SCRIPT="\$POST_INSTALL_$CARD"
	[ -n "$SCRIPT" ] && eval "$SCRIPT"
    ;;
    remove)
	/usr/sbin/alsactl store "$CARD"
    ;;
esac
