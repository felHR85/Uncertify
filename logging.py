import os
from distutils.dir_util import copy_tree
import shutil


_method_declaration = ".method private static createLoggingIntercetor()Lokhttp3/logging/HttpLoggingInterceptor;"
_method_end = ".end method"

_lines = ["\t.locals 2\n", "\tnew-instance v0, Lokhttp3/logging/HttpLoggingInterceptor;\n", "\tinvoke-direct {v0}, Lokhttp3/logging/HttpLoggingInterceptor;-><init>()V\n", "\tsget-object v1, Lokhttp3/logging/HttpLoggingInterceptor$Level;->BODY:Lokhttp3/logging/HttpLoggingInterceptor$Level;\n", "\tinvoke-virtual {v0, v1}, Lokhttp3/logging/HttpLoggingInterceptor;->setLevel(Lokhttp3/logging/HttpLoggingInterceptor$Level;)Lokhttp3/logging/HttpLoggingInterceptor;\n", "\treturn-object v0\n"]

def add_http_logging(app_folder):
    okhttp_folder = _get_okhttp_folder(app_folder)
    _add_logging_folder(okhttp_folder)
    #TODO!!!


def _get_okhttp_folder(app_folder):
    for root, dirs, files in os.walk(app_folder):
        if root.split("/")[-1] is "okhttp3":
            return root


def _add_logging_folder(okhttp_folder):
    shutil.rmtree(okhttp_folder + "/logging", ignore_errors=True)
    copy_tree("logging", okhttp_folder + "/logging")


