from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Repair two JavaScript sequences that were corrupted while the full HTML
# was originally split into restore chunks. Without these fixes the browser
# stops parsing the whole script, so navigation buttons appear to do nothing.
s=s.replace("split(/\\\n\\\\s*\\\n/)", r"split(/\n\s*\n/)")
s=s.replace("p.body.join('\\\n\\\n')", r"p.body.join('\n\n')")

s=s.replace('<button data-r="studio">Studio</button>','')
s=s.replace('Το μήνυμα φτάνει απευθείας στο ιδιωτικό Studio.','Το μήνυμα φτάνει απευθείας σε εμένα.')
s=s.replace('Θα το δω στο ιδιωτικό Studio.','Θα το δω προσωπικά.')
css=Path('olive-accent.css').read_text(encoding='utf-8')
if 'OLIVE ACCENT + STRONGER CTA' not in s:
    s=s.replace('</style>',css+'\n</style>',1)
p.write_text(s,encoding='utf-8')
