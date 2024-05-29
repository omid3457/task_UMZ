import sqlite3
primary_id = 0
con = sqlite3.connect('Expenses')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS expens(
    ID ,
    DATE TEXT,
    PRICE,
    CATEGORY TEXT,
    INFO TEXT,
    PRIMARY KEY(ID)
)""")

def add_one(date, price, category, info):
    global primary_id
    primary_id += 1
    cur.execute('INSERT INTO expens VALUES(?, ?, ?, ?, ?)',(primary_id, date,price,category,info))
    con.commit()
    print('done!!!')

def updte(date1, price1, category1, info1, id1):
    test = (date1, price1, category1, info1, id1)
    cur.execute("""UPDATE expens SET DATE=?,PRICE=?,CATEGORY=?,INFO=? WHERE ID=?
    """,test)
    con.commit()
    print('done!!!')

def show():
    cur.execute('SELECT * FROM expens')
    data = cur.fetchall()
    for i in data:
        print(i)

def delete(id1):
    cur.execute('DELETE FROM expens WHERE ID=?', (id1, ))
    print('done!!!')

while 1:
    print("""1-add
2-update
3-show
4-delete
5-exixt
    """)
    command = int(input('enter command: '))
    if command == 1:
        date = input('enter date: ')
        price = int(input('enter price: '))
        category = input('enter category: ')
        info = input('enter info: ')
        add_one(date, price, category, info)
    elif command == 2:
        id1 = int(input('enter id: '))
        date = input('enter date: ')
        price = int(input('enter price: '))
        category = input('enter category: ')
        info = input('enter info: ')
        updte(date, price, category, info, id1)
    elif command == 3:
        print()
        show()
    elif command == 4:
        id1 = int(input('enter id: '))
        delete(id1)
    elif command == 5:
        print('goodbye!!!!')
        break
    print('*' * 30)
con.close()