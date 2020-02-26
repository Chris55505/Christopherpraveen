
#url = "D:\GIT_Code\job-configuration\brd-validation\Alpha Big SQL Hive DDL Extract\Alpha Big SQL Hive DDL Extract\Hive\hdcwd00p\HiveTableDDL_hdcwd00p.sql"

inf = open("D:/GIT_Code/job-configuration/brd-validation/Alpha Big SQL Hive DDL Extract/Alpha Big SQL Hive DDL Extract/Hive/hdcwd00p/HiveTableDDL_hdcwd00p.sql");

def searcher(outf, inf, string):
    with open(outf, 'a') as f1:
        if string in open(inf).read():
            f1.write(string)


