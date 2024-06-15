import os

def list_files(current_path):
    print("current path: ", current_path)
    paths = []
    dir_items = os.listdir(current_path)
    for item in dir_items:
        full_path = f"{current_path}/{item}"
        if os.path.isfile(full_path):
            paths.append(full_path)
        elif os.path.isdir(full_path):
            paths.extend(list_files(f"{current_path}/{item}"))
    return paths

def main():
    print(list_files("."))


main()
