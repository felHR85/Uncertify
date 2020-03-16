import sys
import xml.etree.ElementTree as ET

def modify_app_manifest(manifest_path: str): 
    manifest_file = manifest_path
    network_security_file = "@xml/network_security_config"

    manifest = ET.parse(manifest_file)

    ET.register_namespace('android', "http://schemas.android.com/apk/res/android")

    root = manifest.getroot()

    app = root.get('application')

    for elem in root.iter():
        if elem.tag == 'application':
            try:
                elem.attrib.pop('{http://schemas.android.com/apk/res/android}networkSecurityConfig')
            except KeyError:
                pass 

            elem.set('android:networkSecurityConfig', network_security_file)


    xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode()
    f = open('AndroidManifest.xml','w')
    f.write(str(xmlstr))
    f.close()