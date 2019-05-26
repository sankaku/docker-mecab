import MeCab
from glob import glob
import re
from os import makedirs
from os.path import dirname
from tqdm import tqdm

DIC_PATH = '/usr/local/lib/mecab'
INPUT_DIR = '/app/input'
OUTPUT_DIR = '/app/output'
FILE_EXTENSION = 'txt'

m = MeCab.Tagger('-d {dic_path} -Owakati -b 16384'.format(dic_path=DIC_PATH))


def get_input_files_paths():
    return glob('{input_dir}/**/*.{extension}'.format(input_dir=INPUT_DIR, extension=FILE_EXTENSION), recursive=True)


def split(path):
    """
    Splits words in the text in `path` by blank
    """
    with open(path, 'r') as f:
        text = f.read()
    return m.parse(text)


def save(path, text):
    with open(path, 'w') as f:
        f.write(text)


def get_new_file_path(old_path):
    """
    Returns the output file path for input file path
    """
    return re.sub(r'^{input_dir}'.format(input_dir=INPUT_DIR), OUTPUT_DIR, old_path)


def mkdirs_for_output(input_files_paths):
    """
    Makes directories to save output files
    """
    output_file_paths = [get_new_file_path(path) for path in input_files_paths]
    output_directories = set([dirname(path) for path in output_file_paths])
    for d in output_directories:
        makedirs(d, exist_ok=True)


if __name__ == '__main__':
    files = get_input_files_paths()
    # Make directories in advance
    mkdirs_for_output(files)
    for _file in tqdm(files):
        text = split(_file)
        new_path = get_new_file_path(_file)
        save(new_path, text)
