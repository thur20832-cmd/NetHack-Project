[app]
title = NetHack DedSec
package.name = nethack
package.domain = org.dedsec
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Requisitos blindados (Python 3.9 e Kivy estável)
requirements = python3,kivy==2.3.0,android,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf

orientation = portrait
fullscreen = 1

# Permissões do Alto Escalão
android.permissions = CAMERA, INTERNET, ACCESS_FINE_LOCATION
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
