from ppadb.client import Client as adb
from optparse import OptionParser
from androguard.misc import AnalyzeAPK
from lxml import etree


#options
parser = OptionParser()
parser.add_option("-H", "--host", dest="host", help="Host of adb, default: 127.0.0.1", default="127.0.0.1")
parser.add_option("-P", "--port", dest="port", help="port of adb, default: 5037", default=5037)
parser.add_option("-d", "--device", dest="device",help="Specify emulator to connect, default: 1st Emulator")
parser.add_option("-l", "--list", dest="list_dev", action="store_true", help="List adb devices")
parser.add_option("-L", "--list-packages", dest="list_packages", action="store_true", help="List installed packages")

#Installing & Uninstalling & is install check
parser.add_option("-i", "--install", dest="install", action="store_true", help="Install an apk with -p path")
parser.add_option("-p", "--path", dest="path", help="Path to apk")
parser.add_option("-u", "--uninstall", dest="uninstall", action="store_true", help="Uninstall an apk with package name -s")
parser.add_option("-I", "--is-installed", dest="is_install", action="store_true", help="Check an apk is installed with package name -s")
parser.add_option("-s", "--source", dest="source", help="Package name, example: com.abc.myapp")


#push or pull
parser.add_option("-U", "--upload", dest="upload", action="store_true", help="Push/Upload files to device -S source -E destination")
parser.add_option("-D", "--download", dest="download", action="store_true", help="Pull/Download files to device -S source -E destination")
parser.add_option("-S", "--usource", dest="usource", help="Source file path to upload/Download")
parser.add_option("-E", "--des", dest="dest", help="Destination file path to upload/Download")

#Extract base apk & AndroidManifest.xml file
parser.add_option("-e", "--extract", dest="extract", action="store_true", help="Extract base.apk & AndroidManifest.xml file with Package name -s")


(options, args) = parser.parse_args()


#initialize connection
client = adb(host=options.host, port=options.port)

#Getting devices
devices = []
def list_devices():
	for device in client.devices():
		devices.append(device.get_serial_no())

#Listing devices
if options.list_dev:
	list_devices()
	for device in devices:
		print("Emulator: ", device)

#Set a device
if options.device == None:
	list_devices()
	device = client.device(devices[0])
else:
	device = client.device(options.device)

#List packages
if options.list_packages:
	print(device.shell("pm list packages"))


#Check installed APK
if options.is_install and options.source != None:
	if device.is_installed(options.source):
		print("Package:", options.source, "is already installed")
	else:
		print("Package:", options.source, "is not installed")
elif options.is_install and options.source == None:
	print("Please provide a package name with -s source option, example: com.abc.myapp")


#Installing APK
if options.install and options.path != None:
	try:
		if device.install(options.path):
			print("App installed succesfully")
	except FileNotFoundError:
		print("Please enter a valid path to APK")
elif options.install and options.path == None:
	print("Please use this option with path -p")
	

#Uninstalling APK
if options.uninstall and options.source != None:
	if device.uninstall(options.source):
		print("Package:", options.source, "is uninstalled successfully")
	else:
		print("Package:", options.source, "is not installed or failed to uninstall")

elif options.uninstall and options.source == None:
	print("Please provide a package name with -s source option, example: com.abc.myapp")


#push a package
if options.upload and options.usource != None and options.dest != None:
	try:
		if device.push(options.usource, options.dest) == None:
			print("File uploaded successfully")
		else:
			print("Upload failed & Please provide full path in destination example: /sdcard/Download/abc.text")
	except RuntimeError:
		print("Upload failed & Please provide full path in destination example: /sdcard/Download/abc.text")


elif options.upload and (options.usource == None or options.dest == None):
	print("Please provide source(upload from) -S and destination(upload to) -E")


#pull a package
if options.download and options.usource != None and options.dest != None:
	try:
		if device.pull(options.usource, options.dest) == None:
			print("File Downloaded successfully")
		else:
			print("Download failed")
	except RuntimeError:
		print("Download failed")


elif options.download and (options.usource == None or options.dest == None):
	print("Please provide source(download from) -S and destination(Download to) -E")



#extract Android manifest file & base apk
if options.extract and options.source:
	path = device.shell("pm path " + options.source)
	if not path.startswith("package:"):
		print("Package", options.source, "not found")
	else:
		apk_path = path.replace("package:", "").strip()
		device.pull(apk_path, "base-"+options.source+".apk")
		print("Package downloaded successfully Name:", "base-"+options.source+".apk")
		apk, d, dx = AnalyzeAPK("base-"+options.source+".apk")
		manifest = apk.get_android_manifest_xml()
		manifest_dom = manifest_str = etree.tostring(manifest, pretty_print=True, encoding='unicode')
		with open(options.source+"-AndroidManifest.xml", "w") as file:
			file.write(manifest_dom)
			file.close()
		print("Written to file:", options.source+"-AndroidManifest.xml")
	


