# PyAutomate

A victim of Automation

Inspired from  `Automate the Boring Stuff with Python: Practical Programming for Total Beginners Book`  by _Al Sweigart_ [link](https://automatetheboringstuff.com/)

## Usage

- On Windows, the shebang line is `#! python3`
- On OS X, the shebang line is `#! /usr/bin/env python3`
- On Linux, the shebang line is `#! /usr/bin/python3`

### Running Python Programs with Assertions Disabled

You can disable the assert statements in your Python programs for a slight
performance improvement. When running Python from the terminal,
include the `-O` switch after python or python3 and before the name of the
`.py` file.

```sh
python ./script.py -O
```

This will run an optimized version of your program that skips the
assertion checks.

## development

```sh
pip3 install send2trash
pip3 install requests
pip3 install beautifulsoup4
pip3 install selenium
pip3 install openpyxl
pip3 install PyPDF2
pip3 install python-docx (install python-docx , not docx )
pip3 install imapclient
pip3 install pyzmail
pip3 install twilio
pip3 install pillow
pip3 install pyobjc-core (on OS X only)
pip3 install pyobjc (on OS X only)
pip3 install python3-xlib (on Linux only)
pip3 install pyautogui
```

## License

BSD-3 License
