import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # insert function
    def insert(self, name, age, doj, email, gender, contact, address):
        # here the qn marks are for placeholder for insertion
        sql = "insert into employees values (NULL,?,?,?,?,?,?,?)"
        self.cur.execute(
            sql, (name, age, doj, email, gender, contact, address))
        self.con.commit()

    # fetch all data form db
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows = self.cur.fetchall()
        print(rows)
        return rows

    # delete a record
    def remove(self, id):
        # for tupple if single element put comma after element
        self.cur.execute("delete from employees where id=?", (id,))

    # updage a record
    def update(self, id, name, age, doj, email, gender, contact, address):
        sql = "update employees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?"
        self.cur.execute(
            sql, (name, age, doj, email, gender, contact, address, id))
        self.con.commit()
