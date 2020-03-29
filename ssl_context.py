import os

init_context_line = "Ljavax/net/ssl/SSLContext;->init([Ljavax/net/ssl/KeyManager;[Ljavax/net/ssl/TrustManager;Ljava/security/SecureRandom;)V"

def modify_ssl_contexts(app_folder):
    detected_files = _search_ssl_contexts(app_folder)
    if len(detected_files) is 0:
        return False
    
    for d in detected_files:
        _edit_file(d)
    
    return True


def _search_ssl_contexts(app_folder):
    detected_files = []
    for root, dirs, files in os.walk(app_folder):
         match_tuple = _file_has_context_sssl(files, root)
         if match_tuple is not None:
             detected_files.append(os.path.join(root, files))
    return detected_files

def _file_has_context_sssl(files, root):
    smali_files = [".smali" in f for f in files]
    for f in smali_files:
        file_lines = open(f, 'r').readlines()
        matches = list(filter(lambda x: init_context_line in x[1], zip(range(len(file_lines)), file_lines)))
        if len(matches) > 0:
            return (os.path.join(root, f), matches)
        else:
            return None

def _edit_file(file_tuple):
    return "TODO!!!!"