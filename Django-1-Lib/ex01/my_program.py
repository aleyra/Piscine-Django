import local_lib.path as path


if __name__ == "__main__":
    folder = "new_dir"
    file = "new_file.txt"
    s = "Je suis le nouveau fichier"
    print("\033[91mlet's go\033[00m")
    try:
        path.Path.mkdir(folder)
        print("\033[91mnew dir created\033[00m")  #
        path.Path.cd(folder)
        print("\033[91min new dir\033[00m")  #
        f = open(file, 'w')
        f.write(s)
        f = open(file, 'r')
        print(f.read())
        print("\033[91mnew file created and filed\033[00m")  #
    except Exception as err:
        print(err)
