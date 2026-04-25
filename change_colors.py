import os
import glob

# Find all HTML files
html_files = glob.glob('*.html')

# New colors: Clean white and blue theme suitable for design
new_bg = 'background-color: #ffffff;'
new_color = 'color: #1e3a8a;'
new_gradient = 'background: #1e3a8a;'
new_teal = 'background-color: #f1f5f9;'
new_dark_teal = 'background-color: #1e3a8a;'
new_var_bg = 'background-color: var(--bg-color, #ffffff);'
new_color_teal = 'color: #1e3a8a;'
new_color_dark = 'color: #1e3a8a;'
new_color_darker = 'color: #1e3a8a;'

# Replace all old colors with new ones
replacements = {
    'background-color: #f8fafc;': new_bg,
    'color: #1e3a8a;': new_color,
    'background: linear-gradient(135deg, #1e3a8a, #60a5fa);': new_gradient,
    'background-color: #e0f2fe;': new_teal,
    'background-color: #1e3a8a;': new_dark_teal,
    'background-color: var(--bg-color, #f8fafc);': new_var_bg,
    'color: #1e3a8a;': new_color_teal,
    'color:#024950;': new_color,
    'color:#015f63;': new_color_dark,
    'color: #013333;': new_color_darker,
}

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements.items():
        content = content.replace(old, new)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Colors updated to clean white and blue theme suitable for the design.")