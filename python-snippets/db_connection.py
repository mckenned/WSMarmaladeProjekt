import pymysql.cursors

def db_connection():
    try:
        #connect to db
        conn = pymysql.connect(host='localhost',
                               user='pyuser',
                               password='secret',
                               db='marmelade',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

        #Datasaving
        with conn.cursor() as cur:
            sql='INSERT INTO...'
            cur.execute(sql,'whatever')
            conn.commit()
            print('ID of new tuble:', cur.lastrowid)

        with conn.cursor() as cur:
            sql='SELECT * FROM mytable'
            cur.execute(sql)
            result=cur.fetchone()
            while result:
                print('ID=%d txt=%s nmb=%d' %
                      (result['id'], result['txt'], result['nmb']))
                result = cur.fetchone()
    except BaseException as ex:
        print('Error: ', ex)
    finally:
        conn.close()
