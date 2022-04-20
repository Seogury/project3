import psycopg2

host = 'ruby.db.elephantsql.com'
user = 'ilqgdpbq'
password = 'Sckj3_rvWDsh6Ydu8mKZXA0Rw3s1osJh'
database = 'ilqgdpbq'

conn = psycopg2.connect(
    host = host, 
    user = user, 
    password = password, 
    database = database
    )

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS cardio;")

cur.execute("""CREATE TABLE cardio (
    id INTEGER,  
    age INTEGER,         
    gender INTEGER,
    height INTEGER,      
    weight FLOAT,
    ap_hi INTEGER,
    ap_lo INTEGER,
    cholesterol INTEGER,
    gluc INTEGER,
    smoke INTEGER,
    alco INTEGER,
    active INTEGER,
    cardio INTEGER)""")

with open('./cardio_train.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(
        f,
        'cardio', 
        sep=',',
        columns= ('id','age','gender','height','weight','ap_hi','ap_lo','cholesterol','gluc','smoke','alco','active','cardio'))

conn.commit()

cur.close()

conn.close()