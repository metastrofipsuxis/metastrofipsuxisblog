from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Repair any literal backslash + real newline sequences that were introduced
# when the original HTML was split into restore chunks. In JavaScript these
# break regex/string literals and stop the entire navigation script.
s=s.replace("\\\n", "\\n")

s=s.replace('<button data-r="studio">Studio</button>','')
s=s.replace('Το μήνυμα φτάνει απευθείας στο ιδιωτικό Studio.','Το μήνυμα φτάνει απευθείας σε εμένα.')
s=s.replace('Θα το δω στο ιδιωτικό Studio.','Θα το δω προσωπικά.')
css=Path('olive-accent.css').read_text(encoding='utf-8')
if 'OLIVE ACCENT + STRONGER CTA' not in s:
    s=s.replace('</style>',css+'\n</style>',1)
p.write_text(s,encoding='utf-8')
