# pyPassSafe

# **🔐 Simple Password Manager**  

A lightweight, secure, and easy-to-use password manager built in Python. This CLI-based application allows you to store, retrieve, and manage your passwords with encryption for enhanced security.  

---

## **🚀 Features**  
✅ AES Encryption using `cryptography` for password security  
✅ Securely stores passwords in a local `passwords.json` file  
✅ Master key management for encrypting and decrypting passwords  
✅ Interactive CLI with a user-friendly interface using `rich` library  
✅ Ability to list stored services  

---

## **📦 Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/Nixantsingh943/pyPassSafe/
cd pyPassSafe
```

### **2. Install Dependencies**  
Ensure you have Python 3 installed, then install required dependencies:  
```bash
pip install -r requirements.txt
```

### **3. Run the Password Manager**  
```bash
python manager.py
```

---

## **🛠 Usage**  

### **1️⃣ Save a New Password**  
- Choose option `1` in the menu  
- Enter the service name (e.g., "Gmail")  
- Enter your username  
- Enter and confirm your password  

### **2️⃣ Retrieve a Stored Password**  
- Choose option `2` in the menu  
- Select the service name  
- View your decrypted credentials  

### **3️⃣ List Stored Services**  
- Choose option `3` to see a list of saved services and usernames  

### **4️⃣ Exit the Program**  
- Choose option `4` to exit  

---

## **🔒 Security Measures**  
- Uses AES encryption with a generated secret key stored in `secret.key`  
- The master key is required to decrypt stored passwords  
- Passwords are stored in an encrypted format in `passwords.json`  

---

## **📂 Project Structure**  
```
📁 password-manager  
 ├── 📄 manager.py  # Main password manager script  
 ├── 📄 secret.key  # Encryption key (auto-generated)  
 ├── 📄 passwords.json  # Encrypted password storage  
 ├── 📄 requirements.txt  # Required dependencies  
 ├── 📄 README.md  # Project documentation  
```

---

## **📜 Dependencies**  
- `cryptography` (for password encryption)  
- `rich` (for interactive CLI interface)  

To install them manually:  
```bash
pip install cryptography rich
```

---

## **🤝 Contributing**  
Feel free to **fork** this repository, submit pull requests, or suggest improvements!  

---
