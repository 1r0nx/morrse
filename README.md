# morrse

**morse is a command line tool** to encode text into morse and decode morse code

---

## 🚀 Features

- enc
- dec
- The separator between letters are spaces
- The separator between words while decoding morse is "/" by default but can be "," or ";"

---

## 🧱 Requirements
You need to have pyinstaller to compile the source code into binary. You can install it with:
```bash
pip3 install pyinstaller
```

---

## 🔧 Installation

Clone the repository and create a binary:
```bash
git clone https://github.com/1r0nx/morrse
cd morrse
chmod +x build.sh
./build.sh
sudo cp dist/morrse /usr/bin
```
You can now use **morrse** as a simple linux commands

Or run it as a script:
```bash
git clone https://github.com/1r0nx/morrse
cd morrse
chmod +x morrse.py
./morrse.py
```


## ⚙️ Example

```bash
morrse enc -s 'this is morse code'
```

Output:

```bash
- .... .. ... / .. ... / -- --- .-. ... . / -.-. --- -.. .
```

```bash
morrse dec -s '- .... .. ... / .. ... / -- --- .-. ... . / -.-. --- -.. .'
```

Output:

```bash
THIS IS MORSE CODE
```

```bash
morrse dec -s '- .... .. ... , .. ... , -- --- .-. ... . , -.-. --- -.. .'
```

Output:

```bash
THIS IS MORSE CODE
```

```bash
morrse dec -s '- .... .. ... ; .. ... ; -- --- .-. ... . ; -.-. --- -.. .'
```

Output:

```bash
THIS IS MORSE CODE
```


## 📜 License

MIT License

---

## 🙋 Contributing

Pull Requests and suggestions are welcome. Please follow standard coding practices and document your changes.

