import os
import shutil
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

def copy_security_file(temp_folder):
    has_xml_dir = os.path.isdir(temp_folder + '/res/xml')
    has_xml_file = os.path.isfile(temp_folder + '/res/xml/network_security_config.xml')

    if has_xml_dir and has_xml_file:
        os.remove(temp_folder + '/res/xml/network_security_config.xml')
        shutil.copyfile('./xml/network_security_config.xml', temp_folder + '/res/xml/network_security_config.xml')
    elif has_xml_dir is not has_xml_file:
        shutil.copyfile('./xml/network_security_config.xml', temp_folder + '/res/xml/network_security_config.xml')
    elif not has_xml_dir:
        os.mkdir(temp_folder + '/res/xml')
        shutil.copyfile('./xml/network_security_config.xml', temp_folder + '/res/xml/network_security_config.xml')
