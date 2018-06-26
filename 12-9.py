import pymysql
db = pymysql.connect( "localhost", "root",  "",  "order_db",
                      use_unicode=True, charset="utf8")       
cursor = db.cursor()
sql = '''INSERT INTO custdetail(name, address, tel)
VALUES ("โครงการบัณฑิตศึกษา", "18/18 ถ.บางนา-ตราด กม.18 บางพลี สมุทรปราการ","0-2337-0361")'''
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
