[app]
title = NetHack DedSec
package.name = nethack
package.domain = org.dedsec
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,android
orientation = portrait
fullscreen = 1
android.permissions = CAMERA, INTERNET, ACCESS_FINE_LOCATION
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
