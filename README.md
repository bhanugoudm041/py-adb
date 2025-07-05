# vulnscan-adb
This tool allows you to do lot of things related to android application pentesting. It can also detect misconfiguration in AndroidManifest.xml file

## Installation
```
git clone https://github.com/bhanugoudm041/vulnscan-adb.git
cd vulnscan-adb
pip3 install -r requirement.txt
python3 vulnscan-adb.py -h
```
#### Simple Options
```
└─$ python3 vulnscan-adb.py -h
Usage: vulnscan-adb.py [options]

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
  -x, --extract-all     Extract all split apk files with Package name -s
  -c COMMAND, --cmd=COMMAND
                        ADB command to run
  -v, --vulns           Analyze the APK and shows info & Misconfigurations
```
![image](https://github.com/user-attachments/assets/3869090b-7940-43da-8bbb-faebe9846d63)

