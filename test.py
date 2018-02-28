from util.mysql import select_table

print(select_table(table="users", column="*", condition="username", value='zh')[0][2])