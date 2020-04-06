import os
from distutils.dir_util import copy_tree
import shutil

okhttp_file_name = 'OkHttpClient.smali'

_method_declaration = ".method private static createLoggingIntercetor()Lokhttp3/logging/HttpLoggingInterceptor;"
_method_end = ".end method"

_lines = ["\t.locals 2\n", "\tnew-instance v0, Lokhttp3/logging/HttpLoggingInterceptor;\n", "\tinvoke-direct {v0}, Lokhttp3/logging/HttpLoggingInterceptor;-><init>()V\n", "\tsget-object v1, Lokhttp3/logging/HttpLoggingInterceptor$Level;->BODY:Lokhttp3/logging/HttpLoggingInterceptor$Level;\n", "\tinvoke-virtual {v0, v1}, Lokhttp3/logging/HttpLoggingInterceptor;->setLevel(Lokhttp3/logging/HttpLoggingInterceptor$Level;)Lokhttp3/logging/HttpLoggingInterceptor;\n", "\treturn-object v0\n"]

def add_http_logging(app_folder):
    okhttp_folders = _get_okhttp_folder(app_folder)

    if len(okhttp_folders) == 0:
        return False

    for folder in okhttp_folders:
        _add_logging_folder(folder)
    
    okhttp_files =_get_okhttp_file(app_folder)
    
    for f in okhttp_files:
        _add_logging_method(f)
        _call_loggin_method(f)

def _get_okhttp_folder(app_folder):
    okhttp_folders = []
    for root, dirs, files in os.walk(app_folder):
        if root.split("/")[-1] is "okhttp3":
            return okhttp_folders.append(root)
    return okhttp_folders

def _add_logging_folder(okhttp_folder):
    shutil.rmtree(okhttp_folder + "/logging", ignore_errors=True)
    copy_tree("logging", okhttp_folder + "/logging")

def _get_okhttp_file(app_folder):
    detected_files = []
    for root, dirs, files in os.walk(app_folder):
        if okhttp_file_name in files:
            path = os.path.join(root, okhttp_file_name)
            detected_files.append(path)
    return detected_files


def _add_logging_method(okhttp_file):
    file_lines = open(okhttp_file, 'r').readlines()

    file_lines.append("\n")
    file_lines.append(_method_declaration)
    for item in _lines:
        file_lines.append(item)
    file_lines.append(_method_end)
    file_lines.append("\n")

    with open(okhttp_file, 'w') as okhttp_file:
        for item in file_lines:
            okhttp_file.write(item)
    return True

def _call_loggin_method(okhttp_file):
    print("TODO")    

