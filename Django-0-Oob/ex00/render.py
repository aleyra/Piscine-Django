import sys
from settings import name, lang1, lang2, lang3, niv_lang1, niv_lang2, niv_lang3, age, profession

def read_template(file):
    try:
        f = open(file, 'r')
    except Exception as err:
        print(err)
        exit()
    code_html = f.read()
    code_html = code_html.format(
        name = name,
        lang1 = lang1,
        lang2 = lang2,
        lang3 = lang3,
        niv_lang2 = niv_lang2,
        niv_lang1 = niv_lang1,
        niv_lang3 = niv_lang3,
        age = age,
        profession = profession
    )
    return code_html


def write_html(s, file):
    dot_place = file.rfind('.')
    new_file = file[0: dot_place] + ".html"
    try:
        f = open(new_file, 'w')
        f.write(s)
    except Exception as err:
        print(err)
        exit()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        write_html(read_template(sys.argv[1]), sys.argv[1])
