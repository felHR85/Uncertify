import os
import click

import manifest

#@click.command()
#@click.option('--apk', default=1, help='Path of the Apk')
#@click.pass_context

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

    #TODO: Edit AndroidManifestl.xml





if __name__ == '__main__':
    main()


