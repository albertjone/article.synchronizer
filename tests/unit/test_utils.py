from article_synchronizer.utils import *


def test_get_excute_dir():
    pass


def test_get_all_files_in_dir():
    target_dir = '/Users/xiaojueguan/Boostnote/notes/'
    files = get_all_files_in_dir(target_dir)
    print(files)

def test_get_all_dirs_in_dir():
    target_dir = '/Users/steveguan/code/Interest/Boostnote/attachments'
    dirs = get_all_dirs_in_dir(target_dir)
    print(dirs)

def test_is_dir_exits():
    pass


def test_is_path_exists():
    pass


def test_get_abs_path():
    pass


def test_remove_slant_before_str():
    pass


def test_concatenate_path():
    pass


def test_load_json_from_file():
    pass


def test_get_file_content():
    file_path = '/Users/xiaojueguan/Boostnote/boostnote.json'
    # content = get_file_content(file_path, file_type=RAW)
    # content = get_file_content(file_path, file_type=JSON)
    file_path = '/Users/xiaojueguan/Boostnote/notes/0c762b83-9100-4e72-a78a-62a4d49d2864.cson'
    content = get_file_content(file_path, file_type=CSON)
    print(content)



# test_get_file_content()
# test_get_all_files_in_dir()
test_get_all_dirs_in_dir()
