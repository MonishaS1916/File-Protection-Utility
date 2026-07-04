# File Protection Utility
import hashlib
import os

HASH_FILE = "hashes.txt"

def generate_hash(file_path):
    sha = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha.update(chunk)

    return sha.hexdigest()


def save_hash(file_path):
    if not os.path.exists(file_path):
        print("❌ File not found.")
        return

    file_hash = generate_hash(file_path)

    with open(HASH_FILE, "a") as f:
        f.write(f"{file_path}|{file_hash}\n")

    print("✅ File protected successfully!")
    print("Hash:", file_hash)


def verify_hash(file_path):
    if not os.path.exists(file_path):
        print("❌ File not found.")
        return

    current_hash = generate_hash(file_path)

    if not os.path.exists(HASH_FILE):
        print("No protected files found.")
        return

    with open(HASH_FILE, "r") as f:
        for line in f:
            saved_file, saved_hash = line.strip().split("|")

            if saved_file == file_path:
                if saved_hash == current_hash:
                    print("🟢 File is SAFE.")
                else:
                    print("🔴 WARNING! File has been modified.")
                return

    print("File not registered.")


while True:
    print("\n====== FILE PROTECTION UTILITY ======")
    print("1. Protect File")
    print("2. Verify File")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        path = input("Enter file path: ")
        save_hash(path)

    elif choice == "2":
        path = input("Enter file path: ")
        verify_hash(path)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")