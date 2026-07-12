book = {}
book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 256545548
}
book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': 564578212
}
import json
s=json.dumps(book)
with open ("C:/Code/jook.txt", "w") as f:
    f.write(s)