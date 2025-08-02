import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('backend/contacts.db')
cursor = conn.cursor()

# Verificar cuántos contactos hay
cursor.execute('SELECT COUNT(*) FROM contacts')
total = cursor.fetchone()[0]
print(f'Total de contactos: {total}')

if total > 0:
    print('\nPrimeros 5 contactos:')
    cursor.execute('SELECT name, email, company, type, created_at FROM contacts LIMIT 5')
    for i, row in enumerate(cursor.fetchall(), 1):
        name, email, company, type_contact, created_at = row
        print(f'{i}. {name} ({email}) - {company} - {type_contact} - {created_at}')
else:
    print('No hay contactos en la base de datos')

conn.close()
