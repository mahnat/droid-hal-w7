# These and other macros are documented in dhd/droid-hal-device.inc
%define device w7
%define vendor lge
%define vendor_pretty LG
%define device_pretty Optimus L90
%define installable_zip 1
%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}
%include rpm/dhd/droid-hal-device.inc
