import os
from distutils.dir_util import copy_tree
import shutil

okhttp_file_name = 'OkHttpClient.smali'

_method_declaration = ".method private static giveMeInterceptors()Ljava/util/List;\n"
_method_end = ".end method\n"

_lines = ["\t.locals 2\n", "\tnew-instance v0, Lokhttp3/logging/HttpLoggingInterceptor;\n", "\tinvoke-direct {v0}, Lokhttp3/logging/HttpLoggingInterceptor;-><init>()V\n", "\tsget-object v1, Lokhttp3/logging/HttpLoggingInterceptor$Level;->BODY:Lokhttp3/logging/HttpLoggingInterceptor$Level;\n", "\tinvoke-virtual {v0, v1}, Lokhttp3/logging/HttpLoggingInterceptor;->setLevel(Lokhttp3/logging/HttpLoggingInterceptor$Level;)Lokhttp3/logging/HttpLoggingInterceptor;\n", "\tnew-instance v1, Ljava/util/ArrayList;\n", "\tinvoke-direct {v1}, Ljava/util/ArrayList;-><init>()V\n", "\tinvoke-interface {v1, v0}, Ljava/util/List;->add(Ljava/lang/Object;)Z\n", "\treturn-object v1\n"]

_constructor = ".method public constructor <init>(Lokhttp3/OkHttpClient$Builder;)V"
_needle = "invoke-virtual {p1}, Lokhttp3/OkHttpClient$Builder;->getInterceptors$okhttp()Ljava/util/List;"

_create_interceptors = "\tinvoke-static {}, Lokhttp3/OkHttpClient;->giveMeInterceptors()Ljava/util/List;\n"

def add_http_logging(app_folder):
    okhttp_folders = _get_okhttp_folder(app_folder)
    if len(okhttp_folders) == 0:
        return False

    for folder in okhttp_folders:
        _add_logging_folder(folder)
    
    okhttp_files =_get_okhttp_file(app_folder)
    
    for f in okhttp_files:
        _add_logging_method(f)
        _call_logging_method(f)
    return True
    

def _get_okhttp_folder(app_folder):
    okhttp_folders = []
    for root, dirs, files in os.walk(app_folder):
        if root.endswith("okhttp3"):
            okhttp_folders.append(root)
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

def _call_logging_method(okhttp_file):
    file_lines = open(okhttp_file, 'r').readlines()
    # Find the line we need to modify
    needle_index = list(filter(lambda x: _needle in x[1] , zip(range(len(file_lines)), file_lines)))[0][0]

    # Check the constructor index
    constructor_index = list(filter(lambda x: _constructor in x[1], zip(range(len(file_lines)), file_lines)))[0][0]

    # Check if the call we need to change is used inside the right constructor
    is_good = len(list(filter(lambda x: ".method" in x[1] and x[0] < needle_index and x[0] > constructor_index, zip(range(len(file_lines)), file_lines)))) == 0

    if is_good == False:
        return False

    # Change line with our own method that creates interceptors
    file_lines[needle_index] = _create_interceptors

    with open(okhttp_file, 'w') as okhttp_file:
        for item in file_lines:
            okhttp_file.write(item)
    return True    

