import sqlite3
import sys
if len(sys.argv) != 3:
    sys.exit(f'Usagi: python {sys.argv[0]} user password')
con = sqlite3.connect('shop.db')
cur = con.execute("SELECT * FROM account WHERE user=? AND password=?", sys.argv[1:])
print('Welcome!' if list(cur) else 'Failed.')
con.close()