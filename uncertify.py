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
    cmd = 'apktool d ' + apk + ' -o ' + temp_folder + " --force > /dev/null"
    os.system(cmd)
    
    print('uncertify: Apk decompiled. Updating Android Manifest')
    manifest_path = temp_folder + "/AndroidManifest.xml"
    manifest.modify_app_manifest(manifest_path)

    os.remove(temp_folder + '/AndroidManifest.xml')
    shutil.copyfile('AndroidManifest.xml', temp_folder + '/AndroidManifest.xml')

    print('uncertify: Manifest updated. Adding network_security_config.xml')

    manifest.copy_security_file(temp_folder)
    
    print('uncertify: network_security_config.xml added. Bypassing certificate pinning')

    #Modify Okhttp file
    okhttp.modify_okhttp(temp_folder)

if __name__ == '__main__':
    main()


