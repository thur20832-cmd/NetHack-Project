[app]
title = NetHack
package.name = nethack
package.domain = org.dedsec
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 1
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
# Vamos focar em apenas UMA arquitetura para ir mais rápido e não dar erro de espaço
android.archs = arm64-v8a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
