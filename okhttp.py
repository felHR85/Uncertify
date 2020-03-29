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
    file_lines = open(okhttp_file, 'r').readlines()

    # Retrieving lines that match method definition and getting index
    filtered_lines = list(filter(lambda x : methods.okhttp_methods[ok_http_method] in x[1], zip(range(len(file_lines)), file_lines)))

    if len(filtered_lines) is 0:
        return False

    line_begin = filtered_lines[0][0]

    # Getting where the method ends
    line_end = list(filter(lambda x: methods.end_method in x[1] and x[0] > line_begin, zip(range(len(file_lines)), file_lines)))[0][0]

    # File substitution
    file_lines[line_begin + 1] = methods.locals_declaration
    file_lines[line_begin + 2] = methods.param_declaration
    file_lines[line_begin + 3] = methods.return_declaration
    
    file_lines = list(map(lambda x: "" if (x[0] > line_begin + 3 and x[0] < line_end) else x[1], zip(range(len(file_lines)), file_lines)))

    with open(okhttp_file, 'w') as okhttp_file:
        for item in file_lines:
            okhttp_file.write(item)
    return True    