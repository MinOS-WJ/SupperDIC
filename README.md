# SupperDIC

## Program Overview

This project consists of two Python programs: `dic.py` and `encrypt_data.py`. They work together to create and query an encrypted dictionary.

## Program Features

### dic.py

A GUI application based on Tkinter for loading and querying encrypted dictionary files. Its main features include:

- **Loading Encrypted Dictionary Files**: Users can select `.dict` files and decrypt them using the corresponding `.key` files.
- **Word Query**: Enter a word in the text box and click the query button or press Enter to display detailed word information, including British and American phonetic symbols and part-of-speech translations.
- **Progress Bar Display**: Shows progress bars when loading dictionaries and querying words for a better user experience.
- **Result Operations**: Provides functions to copy and clear query results for further processing.

### encrypt_data.py

A simple Tkinter application for encrypting CSV formatted dictionary data into `.dict` files and generating corresponding key files `.key`. Its main features include:

- **Selecting CSV Files**: Users can choose CSV files containing word data.
- **Data Encryption**: Uses the XOR encryption algorithm to encrypt CSV data and generates a random key.
- **Saving Encrypted Files and Keys**: Saves encrypted data as `.dict` files and keys as `.key` files.

## Usage

### Runtime Environment

- Python 3.x
- Tkinter library (usually installed with Python)
- base64 module
- csv module
- random module
- os module
- time module

### Running Steps

1. **Encrypt Dictionary Data**:
   - Run `encrypt_data.py`.
   - Click the "Select CSV file and encrypt" button to choose a CSV file with word data.
   - The program automatically generates `.dict` and `.key` files in the same directory.

2. **Query Words**:
   - Run `dic.py`.
   - Click the "Select dictionary file" button to choose the generated `.dict` file.
   - Enter the word you want to query in the input box and click the "Query" button or press Enter.
   - View the query results and use the "Copy result" or "Clear result" buttons for further operations.

## Program Principles

### Encryption and Decryption

- **Encryption**: `encrypt_data.py` reads CSV file data, generates a random 16-byte key, encrypts the data using the XOR encryption algorithm. The encrypted data and key are saved as `.dict` and `.key` files after Base64 encoding.
- **Decryption**: `dic.py` reads the `.dict` and `.key` files, decodes the Base64 data and key, and decrypts using the XOR encryption algorithm to obtain the original dictionary data.

### Query Logic

- `dic.py` stores decrypted data in a dictionary when loading, with the key being the lowercase word and the value being a list of detailed word information.
- During querying, it looks up the input word in the dictionary, displays formatted information if found, otherwise shows a "word not found" message.

## Security Note

This program uses the XOR encryption algorithm, which is simple to implement but has low security and is only suitable for basic data protection needs. For highly sensitive data in practical applications, it is recommended to use more advanced encryption algorithms (such as AES).

## Summary

This project implements dictionary data encryption and query functions through two programs. `encrypt_data.py` encrypts CSV formatted dictionary data into secure `.dict` files, and `dic.py` provides a user-friendly GUI for easy word querying. The entire process is simple and efficient, suitable for small dictionary applications or learning projects.
