
import sqlite3

conn = sqlite3.connect('database/mahasiswa.db')

c = conn.cursor()

# c.execute("""CREATE TABLE mahasiswa (
#         nim INTEGER,
#         full_name TEXT
#         )""")

# c.execute("""INSERT INTO mahasiswa
#           VALUES
#           (1203210010, 'ADE DIAN SUKMANA'),
#           (1203210080, 'ADITYA AULIA ROHMAN'),
#           (1203210101, "AHMAD MU'MIN FAISAL"),
#           (1203210061, 'AISYA DWI AZAHRA'),
#           (1203210068, 'ALIF RIZKY'),
#           (1203210082, 'AMAM RACHMANTO'),
#           (1203210019, 'ANDIKA PUTRA ARIANSYAH'),
#           (1203210049, 'AQILAH PUTRI ALIFAH'),
#           (1203210063, 'DARA ILMA DEUDOENA'),
#           (1203210050, "DHARMA MAR'IE SATOTO")
#           """)

c.execute("SELECT * FROM mahasiswa")
x = c.fetchall()
print(x)

conn.commit()

conn.close()



# c.execute("SELECT * FROM employees WHERE lname='Schafer'")
# print(c.fetchone())