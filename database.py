import mysql.connector


class DbConnection:

    def __init__(self, database, user, password, host):
        self.__database = database
        self.__user = user
        self.__password = password
        self.__host = host

    def db_try_to_connect(self):
        try:
            return mysql.connector.connect(database=self.__database, user=self.__user, password=self.__password,
                                           host=self.__host)

        except mysql.connector.Error as err:
            print(err)

    @staticmethod
    def get_urls():
        project_query = f'SELECT id, attachment FROM images_to_rec'
        with conn.cursor() as curs:
            try:
                curs.execute(project_query)
                return curs.fetchall()

            except mysql.connector.Error as err:
                print(err)

    @staticmethod
    def insert_text(text_collections):
        with conn.cursor() as curs:
            for item in text_collections:
                query = f"UPDATE images_to_rec SET text=%s WHERE id=%s"
                values = (item[1], item[0])

                curs.execute(query, values)

            conn.commit()
            print(f"{curs.rowcount} record(s) updated successfully.")


dbconnection = DbConnection(database='tagclouddb', user='gastinha', password='Gastinh@', host='localhost')
conn = dbconnection.db_try_to_connect()