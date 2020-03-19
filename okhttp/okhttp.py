import os
import fnmatch

# constants
okhttp_file_name = 'OkHttpClient$Builder.smali'

# constants
begin_method = ".method public certificatePinner(Lokhttp3/CertificatePinner;)Lokhttp3/OkHttpClient$Builder"
end_method = ".end method"

# injects
line_1 = ".locals2"
line_2 = ".param p1, \"certificatePinner\""
line_3 = "return-object p0"

def modify_okhttp(app_folder):
    f = _get_okhttp_file(app_folder)

    if f == '':
        return False
    
def _get_okhttp_file(app_folder):
    for root, dirs, files in os.walk(app_folder):
        if okhttp_file_name in files:
            return os.path.join(root, okhttp_file_name)
        else:
            return ''

def _edit_okhttp_file(okhttp_file):
    i = 0
    with open("file.txt") as search:
        for line in search:
            print('TODO') # find begin method and end method



