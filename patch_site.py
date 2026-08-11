from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Repair JavaScript sequences corrupted in the original restore chunks.
# They contain a literal backslash followed by a real newline; browsers
# then fail to parse the script and all navigation buttons stop working.
s=s.replace("split(/\\\n\s*\\\n/)", r"split(/\n\s*\n/)")
s=s.replace("p.body.join('\\\n\\\n')", r"p.body.join('\n\n')")

s=s.replace('<button data-r="studio">Studio</button>','')
s=s.replace('Το μήνυμα φτάνει απευθείας στο ιδιωτικό Studio.','Το μήνυμα φτάνει απευθείας σε εμένα.')
s=s.replace('Θα το δω στο ιδιωτικό Studio.','Θα το δω προσωπικά.')
css=Path('olive-accent.css').read_text(encoding='utf-8')
if 'OLIVE ACCENT + STRONGER CTA' not in s:
    s=s.replace('</style>',css+'\n</style>',1)
p.write_text(s,encoding='utf-8')
