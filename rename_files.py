import os


def main():
    i = 0
    path = "C:/my_develop2/python_basic/files/"
    for filename in os.listdir(path):
        my_dest = "textfile_" + str(i) + ".txt"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1


if __name__ == "__main__":
    main()
