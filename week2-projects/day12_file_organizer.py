import os
import shutil

# Dosya türleri
FILE_TYPES = {
    "images": [".png", ".jpg", ".jpeg", ".gif"],
    "documents": [".pdf", ".docx", ".txt"],
    "videos": [".mp4", ".mkv", ".avi"],
    "archives": [".zip", ".rar"],
}


def organize_folder(path):
    if not os.path.exists(path):
        print("Klasör bulunamadı.")
        return

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isdir(file_path):
            continue

        moved = False

        for folder, extensions in FILE_TYPES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                target_folder = os.path.join(path, folder)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"{filename} → {folder}/")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(path, "others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)

            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"{filename} → others/")


def main():
    path = input("Düzenlenecek klasör yolu: ")
    organize_folder(path)
    print("Tamamlandı!")


if __name__ == "__main__":
    main()