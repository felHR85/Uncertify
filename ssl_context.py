import os

init_context_line = "Ljavax/net/ssl/SSLContext;->init([Ljavax/net/ssl/KeyManager;[Ljavax/net/ssl/TrustManager;Ljava/security/SecureRandom;)V"

def modify_ssl_contexts(app_folder):
    _search_ssl_contexts(app_folder)
    return True


def _search_ssl_contexts(app_folder):
    for root, dirs, files in os.walk(app_folder):
        _file_has_context_sssl(files, root)

def _file_has_context_sssl(files, root):
    smali_files = [".smali" in f for f in files]
    for f in smali_files:
        file_lines = open(f, 'r').readlines()
        tuple_lines = zip(range(len(file_lines)), file_lines)
        list_ocurrence = list(filter(lambda x: init_context_line in x[1], tuple_lines))

        if len(list_ocurrence) == 0:
            break
        
        ocurrence = list_ocurrence[0]
        index_begin_method = list(filter(lambda x: ".method" in x[1] and x[0] < ocurrence , tuple_lines))[-1][0]
        index_end_method = list(filter(lambda x: ".end method" in x[1] and x[0] > ocurrence, tuple_lines))[0][0]

        # Increase local variables
        current_locals = int(file_lines[index_begin_method + 1].split(1))
        current_locals = current_locals + 1
        file_lines[index_begin_method + 1] = ".locals " + str(current_locals)

        file_lines.insert(ocurrence -1, "const/4 v" + str(current_locals - 1) + ", 0x0")

        #TODO: Put created register in init method
        #TODO: Write file
        #TODO: Return tuples with info???
    