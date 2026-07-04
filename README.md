# 🔐 File Protection Utility

A simple Python-based File Protection Utility that ensures file integrity by generating and verifying **SHA-256 hashes**. The application helps detect unauthorized modifications to files by comparing their current hash with a previously stored hash.

---

## 🚀 Features

- 📂 Protect any file using SHA-256 hashing
- 🔍 Verify file integrity
- 🛡️ Detect file modifications
- 💾 Store file hashes locally
- 🖥️ Interactive command-line interface
- ⚡ Lightweight and easy to use

---

## 🛠️ Technologies Used

- Python 3
- hashlib (Built-in)
- os (Built-in)

> No external libraries are required.

---

## 📂 Project Structure

```
File-Protection-Utility/
│
├── file_protection_utility.py
├── hashes.txt
├── sample.txt
├── README.md
└── requirements.txt
```

---

## ⚙️ How It Works

### Step 1: Protect a File

The user selects a file, and the application generates a **SHA-256 hash**. The hash is then stored in a local database (`hashes.txt`).

---

### Step 2: Verify a File

The application generates a new hash for the selected file and compares it with the previously stored hash.

- If both hashes match:
  - 🟢 The file is safe and has not been modified.

- If the hashes do not match:
  - 🔴 The file has been altered or tampered with.

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/File-Protection-Utility.git
```

### Navigate to the Project Folder

```bash
cd File-Protection-Utility
```

### Run the Program

```bash
python file_protection_utility.py
```

or

```bash
py file_protection_utility.py
```

---

## 💻 Example

### Main Menu

```
====== FILE PROTECTION UTILITY ======

1. Protect File
2. Verify File
3. Exit

Enter choice:
```

### Protect a File

**Input**

```
1
sample.txt
```

**Output**

```
✅ File protected successfully!

Hash:
9c56cc51d4b6d0b4d87...
```

---

### Verify the File

**Input**

```
2
sample.txt
```

**Output**

```
🟢 File is SAFE.
```

---

### After Modifying the File

**Output**

```
🔴 WARNING! File has been modified.
```

---

## 🔒 Security Concept

This project uses the **SHA-256 cryptographic hash algorithm** to create a unique fingerprint for each file. Even a small change in the file content produces a completely different hash value, making it possible to detect unauthorized modifications.

---

## 📌 Applications

- File Integrity Monitoring
- Digital Forensics
- Cybersecurity Learning
- Software Integrity Verification
- Detecting Unauthorized File Changes
- Secure File Management

---

## 📚 Learning Outcomes

By completing this project, you will gain practical knowledge of:

- Python File Handling
- SHA-256 Hashing
- Cryptographic Hash Functions
- Data Integrity Verification
- Cybersecurity Fundamentals
- Exception Handling

---

## 🚀 Future Enhancements

- AES File Encryption & Decryption
- Password-Protected Files
- GUI using Tkinter
- Multiple Hash Algorithm Support (MD5, SHA-1, SHA-512)
- Real-Time File Monitoring
- Backup and Restore Hash Database
- Export Verification Reports (PDF/CSV)
- Automatic Folder Integrity Scanning

---

## ⚠️ Disclaimer

This project is intended for **educational purposes only**. It demonstrates how cryptographic hashing can be used to verify file integrity. It is not a replacement for enterprise-grade file integrity monitoring solutions.

---

## 👩‍💻 Author

**Monisha S**

Bachelor of Engineering – Computer Science and Engineering (Cybersecurity)

RMK College of Engineering and Technology

---

## ⭐ If you found this project helpful, consider giving it a Star on GitHub!
