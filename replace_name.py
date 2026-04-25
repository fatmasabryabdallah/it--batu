import os
import glob

# Find all HTML files
html_files = glob.glob('*.html')

# Replace the text
old_text = '©تم انشاء هذا الموقع بواسطه رحمه سامح'
new_text = '©تم انشاء هذا الموقع بواسطه Fatma Sabry Abdallah'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace(old_text, new_text)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Replaced in all HTML files.")