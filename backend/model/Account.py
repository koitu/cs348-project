from utils import mysql_connection

#returns true if the user exists
def check_account(username: str, password: str, fuzzy=True):
    with mysql_connection() as con, con.cursor() as cursor:
        find_user = f"""select account_id
                        from account
                        where username = '{username}'
                        and acc_pass = '{password}' """
        cursor.execute(find_user)
        result = cursor.fetchall()
        return result
