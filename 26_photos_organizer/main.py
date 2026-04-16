import os

def rename_files(folder_path, base_name, extension):
    print(os.listdir(folder_path))

    count = 1
    for file in os.listdir(folder_path):
        print(file)
        full_path = os.path.join(folder_path, file)
        print(full_path)
        
        ext = os.path.splitext(file)[1].lower()
        print(ext)

        if extension == ext:
            dest_path = os.path.join(folder_path , (f"{base_name}_{count}{extension}"))
            print(dest_path)
            os.rename(full_path, dest_path)
            count += 1 

if __name__ == "__main__":
    folder = input("Enter the folder path or leave blank: ").strip()
    folder = folder or os.getcwd()
    print(folder)

    base_name = input("Enter a base name for the files: ")
    extension = input("Enter a file extension to filter: ")
    

    if not os.path.isdir(folder):
        print("Invalid directory")
    else:
        rename_files(folder, base_name, extension)
        print("✅ sorting completed")

    


    