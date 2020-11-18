def select_all(table_name):
        select_all = f"select * from {table_name}"
        return select_all

def select_top(n, table_name):
        select_n = f"select top({n}) * from {table_name}"
        return select_n

def get_last_synctime():
        last_synctime = f"select top 1 DateTime from UUTResults order by Datetime desc"
        return last_synctime

def select_from_synctime(table_name, synctime):
        select_all = f"select * from {table_name} where Datetime > '{synctime}'"
        return select_all