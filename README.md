# py-adb
This tool allows you to do lot of things
```
└─$ python3 py-adb.py -h
Usage: py-adb.py [options]

Options:
  -h, --help            show this help message and exit
  -H HOST, --host=HOST  Host of adb, default: 127.0.0.1
  -P PORT, --port=PORT  port of adb, default: 5037
  -d DEVICE, --device=DEVICE
                        Specify emulator to connect, default: 1st Emulator
  -l, --list            List adb devices
  -L, --list-packages   List installed packages
  -i, --install         Install an apk with -p path
  -p PATH, --path=PATH  Path to apk
  -u, --uninstall       Uninstall an apk with package name -s
  -I, --is-installed    Check an apk is installed with package name -s
  -s SOURCE, --source=SOURCE
                        Package name, example: com.abc.myapp
  -U, --upload          Push/Upload files to device -S source -E destination
  -D, --download        Pull/Download files to device -S source -E destination
  -S USOURCE, --usource=USOURCE
                        Source file path to upload/Download
  -E DEST, --des=DEST   Destination file path to upload/Download
  -e, --extract         Extract base.apk & AndroidManifest.xml file with
                        Package name -s

```
![image](https://github.com/user-attachments/assets/54464bb5-fda1-41fe-9000-42807d11c14f)
