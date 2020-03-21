import os
import shutil
import click

import manifest
import okhttp

temp_folder = "./__temp_folder__"


@click.command()
@click.argument("apk")
def main(apk: str):
    print('uncertify: decompiling ' + apk.split('.')[0])
    cmd = 'apktool d ' + apk + '-o ' + temp_folder + " --force > /dev/null"
    os.system(cmd)
    
    print('uncertify: Apk decompiled. Updating Android Manifest')
    manifest_path = temp_folder + "/AndroidManifest.xml"
    manifest.modify_app_manifest(manifest_path)

    os.remove(temp_folder + '/AndroidManifest.xml')
    shutil.copyfile('AndroidManifest.xml', temp_folder + '/AndroidManifest.xml')

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
    
    #Modify Okhttp files





if __name__ == '__main__':
    main()


