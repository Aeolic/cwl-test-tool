import argparse
import os


def main():
    parser = argparse.ArgumentParser(
        "Test Tool for CWL workflow")

    parser.add_argument("files", nargs="*")
    args = parser.parse_args()
    files = args.files

    print("Start iterating through input files!")

    flag = False
    for root, dirs, files in os.walk("/input"):
        for file in files:
            print(file)
            flag = True

    if not flag:
        print("EMPTY INPUT FOLDER!")

    for i, file_path in enumerate(files):
        print("Got file:" + file_path)
        with open(file_path, "r") as f:
            with open("/app/output/file_" + str(i) + ".txt", "w") as w:
                w.write(f.read() + " APPENDED TEXT")
                print("Wrote to File: " + "/app/output/file_" + str(i) + ".txt")

    with open("/app/output/additionalFile.txt", "w+") as w2:
        w2.write("ADDITIONAL FILE")
        print("Wrote to additional File!")


if __name__ == '__main__':
    main()
