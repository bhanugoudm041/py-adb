# py-adb
This tool allows you to do lot of things
```
└─$ python3 py-adb.py -h</br>
Usage: py-adb.py [options]</br>
</br>
Options:</br>
  -h, --help            show this help message and exit</br>
  -H HOST, --host=HOST  Host of adb, default: 127.0.0.1</br>
  -P PORT, --port=PORT  port of adb, default: 5037</br>
  -d DEVICE, --device=DEVICE</br>
                        Specify emulator to connect, default: 1st Emulator</br>
  -l, --list            List adb devices</br>
  -L, --list-packages   List installed packages</br>
  -i, --install         Install an apk with -p path</br>
  -p PATH, --path=PATH  Path to apk</br>
  -u, --uninstall       Uninstall an apk with package name -s</br>
  -I, --is-installed    Check an apk is installed with package name -s</br>
  -s SOURCE, --source=SOURCE</br>
                        Package name, example: com.abc.myapp</br>
  -U, --upload          Push/Upload files to device -S source -E destination</br>
  -D, --download        Pull/Download files to device -S source -E destination</br>
  -S USOURCE, --usource=USOURCE</br>
                        Source file path to upload/Download</br>
  -E DEST, --des=DEST   Destination file path to upload/Download</br>
  -e, --extract         Extract base.apk & AndroidManifest.xml file with</br>
                        Package name -s</br>
</br>
```
![image](https://github.com/user-attachments/assets/54464bb5-fda1-41fe-9000-42807d11c14f)
