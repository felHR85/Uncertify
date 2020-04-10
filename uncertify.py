import os
import shutil
import click

import manifest
import okhttp
import okhttp_methods as methods
import ssl_context
import logging

temp_folder = "./__temp_folder__"
apk_name = "app-temp.apk"
android_manifest_temp = "AndroidManifest.xml"

@click.command()
@click.argument("apk")
@click.option("--pinning", is_flag=True, help="bypass certificate pinning")
@click.option("--interceptors", is_flag=True, help="bypass Okhttp interceptors")
@click.option("--dns", is_flag=True, help="delete dns configuration in Okhttp")
@click.option("--follow", is_flag=True, help="delete follow redirects in Okhttp")
@click.option("--logs", is_flag=True, help="Activate logs in Okhttp")
def main(apk, pinning, interceptors, dns, follow, logs):
    print('uncertify: decompiling ')
    delete_temp()
    cmd = 'apktool d ' + apk + ' -o ' + temp_folder + " --force > /dev/null"
    os.system(cmd)
    
    print('uncertify: Apk decompiled. Updating Android Manifest')
    manifest_path = temp_folder + "/AndroidManifest.xml"
    manifest.modify_app_manifest(manifest_path)

    os.remove(temp_folder + '/AndroidManifest.xml')
    shutil.copyfile('AndroidManifest.xml', temp_folder + '/AndroidManifest.xml')

    print('uncertify: Manifest updated. Adding network_security_config.xml')

    manifest.copy_security_file(temp_folder)
    
    print('uncertify: network_security_config.xml added')

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
            print("uncertify: OkHttp deleted interceptors")
        else:
            print("uncertify: OkHttp not found")

    if dns:
        dns_result = okhttp.modify_okhttp(temp_folder, methods.dns)
        if dns_result:
            print("uncertify: OkHttp deleted dns")
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

    #Add Http logs if app uses OkHttp
    if logs:
        logging.add_http_logging(temp_folder)
    
    print("uncertify: Rebuilding apk")
    rebuild_apk(apk_name)
    delete_temp()

    print("uncertify: Apk rebuild with name app-uncertify.apk")

def rebuild_apk(apk_name):
    cmd = "apktool b " + "__temp_folder__" + " -o " + apk_name + " > /dev/null"
    os.system(cmd)
    
    cmd = "jarsigner -tsa http://timestamp.comodoca.com/rfc3161 -storepass 123456 -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore uncertify.keystore " + apk_name + " felhr85 > /dev/null"
    os.system(cmd)

    cmd = "zipalign -f -v 4 " + apk_name + " " + "app-uncertify.apk"
    os.system(cmd)

def delete_temp():
    shutil.rmtree(temp_folder, ignore_errors=True)
    if os.path.exists(apk_name):
        os.remove(apk_name)
    if os.path.exists(android_manifest_temp):
        os.remove(android_manifest_temp)

if __name__ == '__main__':
    main()


