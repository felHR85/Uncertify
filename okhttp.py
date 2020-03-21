import os
import fnmatch

# constants
okhttp_file_name = 'OkHttpClient$Builder.smali'

# constants
begin_method = ".method public certificatePinner(Lokhttp3/CertificatePinner;)Lokhttp3/OkHttpClient$Builder"
end_method = ".end method"

# injects
line_1 = "\t.locals 2\n"
line_2 = "\t.param p1, \"certificatePinner\"\n"
line_3 = "\treturn-object p0\n"

def modify_okhttp(app_folder):
    f = _get_okhttp_file(app_folder)
    if f == '':
        return False
    _edit_okhttp_file(f)
    return True

    
def _get_okhttp_file(app_folder):
    for root, dirs, files in os.walk(app_folder):
        if okhttp_file_name in files:
            return os.path.join(root, okhttp_file_name)
    return ''

def _edit_okhttp_file(okhttp_file):
    i = 0
    line_begin = 0
    line_end = 0

    file_lines = open(okhttp_file, 'r').readlines()
    for line in file_lines:
        if begin_method in line:
            line_begin = i
        elif (end_method in line) and line_begin is not 0:
            line_end = i
            break
        i = i +1

    if line_begin is 0:
        return False
    
    file_lines[line_begin + 1] = line_1
    file_lines[line_begin + 2] = line_2
    file_lines[line_begin + 3] = line_3
    
    for j in range(line_begin + 4, line_end):
        file_lines[j] = ""

    with open(okhttp_file, 'w') as okhttp_file:
        for item in file_lines:
            okhttp_file.write(item)
    return True    