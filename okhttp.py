import os
import fnmatch

import okhttp_methods as methods

# constants
okhttp_file_name = 'OkHttpClient$Builder.smali'

def modify_okhttp(app_folder, method):
    files = _get_okhttp_file(app_folder)
    if len(files) == 0:
        return False
    
    for f in files:
        _edit_okhttp_file(f, method)

    return True

    
def _get_okhttp_file(app_folder):
    detected_files = []
    for root, dirs, files in os.walk(app_folder):
        if okhttp_file_name in files:
            path = os.path.join(root, okhttp_file_name)
            detected_files.append(path)
    return detected_files

def _edit_okhttp_file(okhttp_file, ok_http_method):
    i = 0
    line_begin = 0
    line_end = 0

    file_lines = open(okhttp_file, 'r').readlines()
    for line in file_lines:
        if methods.okhttp_methods[ok_http_method] in line:
            line_begin = i
        elif (methods.end_method in line) and line_begin is not 0:
            line_end = i
            break
        i = i +1

    if line_begin is 0:
        return False
    
    file_lines[line_begin + 1] = methods.locals_declaration
    file_lines[line_begin + 2] = methods.param_declaration
    file_lines[line_begin + 3] = methods.return_declaration
    
    for j in range(line_begin + 4, line_end):
        file_lines[j] = ""

    with open(okhttp_file, 'w') as okhttp_file:
        for item in file_lines:
            okhttp_file.write(item)
    return True    