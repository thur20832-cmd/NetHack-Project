[app]

# (str) Title of your application
title = NetHack DedSec

# (str) Package name
package.name = nethack

# (str) Package domain (needed for android/ios packaging)
package.domain = org.dedsec

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,android

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = CAMERA, INTERNET, ACCESS_FINE_LOCATION

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (bool) Accept SDK license
android.accept_sdk_license = True

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) skip update of the window during the build
android.skip_update = False

# (str) python-for-android branch to use
p4a.branch = master

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
