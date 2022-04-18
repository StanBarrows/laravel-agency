def file_exists(path):
    from os.path import exists
    file_exists = exists(path)
    return file_exists


def load_json(path):
    if not file_exists(path):
        import sys
        sys.exit('File path not found: ' + path)

    import json
    file = open(path)
    data = json.load(file)
    file.close()
    return data


def update_key_value(path, key, value):
    if not file_exists(path):
        import sys
        sys.exit('File path not found: ' + path)

    import os, dotenv

    dotenv.load_dotenv(path)
    os.environ[key] = value
    dotenv.set_key(path, key, os.environ[key])


def copy_file(sourcePath, targetPath, ):
    if not file_exists(sourcePath):
        import sys
        sys.exit('File path not found: ' + sourcePath)
    import os
    os.system('cp -R ' + sourcePath + ' ' + targetPath)
