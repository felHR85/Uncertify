import os
import shutil
import click

import manifest
import okhttp
import okhttp_methods as methods
import ssl_context

temp_folder = "./__temp_folder__"

@click.command()
@click.argument("apk")
@click.option("--pinning", is_flag=True)
@click.option("--interceptors", is_flag=True)
@click.option("--dns", is_flag=True)
@click.option("--follow", is_flag=True)
def main(apk, pinning, interceptors, dns, follow):
    apk_name = "app-temp.apk" #TODO: detect apk name
    print('uncertify: decompiling ')
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
    if pinning:
        pinning_result = okhttp.modify_okhttp(temp_folder, methods.certificate_pinner)
        if pinning_result:
            print("uncertify: OkHttp certificate pinning bypassed")
        else:
            print("uncertify: OkHttp not found")

    if interceptors:
        interceptor_result = okhttp.modify_okhttp(temp_folder, methods.add_interceptor)
        if interceptor_result:
            print("uncertify: OkHttp certificate pinning bypassed")
        else:
            print("uncertify: OkHttp not found")

    if dns:
        dns_result = okhttp.modify_okhttp(temp_folder, methods.dns)
        if dns_result:
            print("uncertify: OkHttp certificate pinning bypassed")
        else:
            print("uncertify: OkHttp not found")

    if follow:
        follow_result = okhttp.modify_okhttp(temp_folder, methods.follow_redirects)
        follow_ssl_result = okhttp.modify_okhttp(temp_folder, methods.follow_ssl_redirects)
        if follow_result and follow_ssl_result:
            print("uncertify: OkHttp certificate pinning bypassed")
        else:
            print("uncertify: OkHttp not found")

    #Modify SSLContext
    if pinning:
        ssl_context.modify_ssl_contexts(temp_folder)
    
    #Rebuild Apk
    cmd = "apktool b " + "__temp_folder__" + " -o " + apk_name + " > /dev/null"
    os.system(cmd)
    
    cmd = "jarsigner -tsa http://timestamp.comodoca.com/rfc3161 -storepass 123456 -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore uncertify.keystore " + apk_name + " felhr85 > /dev/null"
    os.system(cmd)

    cmd = "zipalign -f -v 4 " + apk_name + " " + "app-uncertify.apk"
    os.system(cmd)

    #TODO: Delete temp files

if __name__ == '__main__':
    main()


