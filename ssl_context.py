import os
import re

init_context_line = "Ljavax/net/ssl/SSLContext;->init([Ljavax/net/ssl/KeyManager;[Ljavax/net/ssl/TrustManager;Ljava/security/SecureRandom;)V"

def modify_ssl_contexts(app_folder):
    modified_files = _search_ssl_contexts(app_folder)
    return len(modified_files) > 0


def _search_ssl_contexts(app_folder):
    modified_files = []
    for root, dirs, files in os.walk(app_folder):
        if "okhttp3" in root == False:
            modified_files.append(_bypass_ssl_context_init(files))
    return modified_files

def _bypass_ssl_context_init(files):
    files_modified = []
    smali_files = [".smali" in f for f in files]
    for f in smali_files:
        file_lines = open(f, 'r').readlines()
        tuple_lines = zip(range(len(file_lines)), file_lines)
        list_ocurrence = list(filter(lambda x: init_context_line in x[1], tuple_lines))

        if len(list_ocurrence) == 0:
            break
        
        for i in list_ocurrence:
            ocurrence = list_ocurrence[i][0]
            index_begin_method = list(filter(lambda x: ".method" in x[1] and x[0] < ocurrence , tuple_lines))[-1][0]

            # Increase local variables
            current_locals = int(file_lines[index_begin_method + 1].split(1))
            current_locals = current_locals + 1
            file_lines[index_begin_method + 1] = ".locals " + str(current_locals)

            # Set the last vX register to null
            dummy_register = "v" + str(current_locals - 1)
            dummy_register_value = "const/4 v" + dummy_register + ", 0x0"
            file_lines.insert(ocurrence -1, dummy_register_value)

            # Get all vX and pX used in the invocation of SSLContext init method
            line = file_lines[ocurrence]
            findings = re.findall("v[0-9]+|p[0-9]+", line)

            # Replace all of them except the first one for our dummy register
            line = line.replace(findings[1], dummy_register)
            line = line.replace(findings[2], dummy_register)
            line = line.replace(findings[3], dummy_register)

            file_lines[ocurrence] = line

        with open(f, 'w') as smali_file:
            for item in file_lines:
                smali_file.write(item)
        
        files_modified[i] = (ocurrence, f)
        
    return files_modified
    