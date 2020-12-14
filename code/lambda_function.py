import sys
import logging
import rds_config
import pymysql

def lambda_handler(event, context):
    runQuery()

def openConnection0():
    try:
        pymysql.connect(host=rds_host,user=db_username,passwd=db_password,db="recordstore")
        logger.info("SUCCESS: Connection 1 to RDS MySQL opened successfully")
    except pymysql.MySQLError as e:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logger.error(e)
        sys.exit()
        
def openConnection1():
    try:
        pymysql.connect(host=rds_host,user=db_username,passwd=db_password,db="mysql")
        logger.info("SUCCESS: Connection 1 to RDS MySQL opened successfully")
    except pymysql.MySQLError as e:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logger.error(e)
        sys.exit()
        
def openConnection2():
    try:
        pymysql.connect(host=rds_host,user=db_username,passwd=db_password,db="information_schema")
        logger.info("SUCCESS: Connection 2 to RDS MySQL opened successfully")
    except pymysql.MySQLError as e:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logger.error(e)
        sys.exit()
        
def openConnection3():
    try:
        pymysql.connect(host=rds_host,user=db_username,passwd=db_password,db="sys")
        logger.info("SUCCESS: Connection 3 to RDS MySQL opened successfully")
    except pymysql.MySQLError as e:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logger.error(e)
        sys.exit()

def runQuery():
    #Database connection settings
    rds_host  = rds_config.rds_host
    db_username = rds_config.db_username
    db_password = rds_config.db_password
    
    #Open database connection
    mydb0 = pymysql.connect(host=rds_host,user=db_username,passwd=db_password,db="recordstore")
    mydb1 = pymysql.connect(host=rds_host,user=db_username,passwd=db_password,db="mysql")
    mydb2 = pymysql.connect(host=rds_host,user=db_username,passwd=db_password,db="information_schema")
    mydb3 = pymysql.connect(host=rds_host,user=db_username,passwd=db_password,db="sys")
    
    
    cursor0 = mydb0.cursor()
    '''
    result0 = cursor0.execute ("SELECT singers.id, singers.name, singers.nationality, records.title \
                                FROM singers \
                                INNER JOIN records on records.recordid = singers.recordid \
                                WHERE records.title LIKE 'Liberian%';")

    record0 = cursor0.fetchone()
    '''
    
    result0 = cursor0.execute("create table demo (id int(11) NOT NULL AUTO_INCREMENT, PRIMARY KEY (id)) AUTO_INCREMENT=1;")
    print (result0)
    res0 = cursor0.execute("drop table demo;")
    print(res0)
    #print(record0)
    mydb0.commit()
    
    cursor1 = mydb1.cursor()
    result1 = cursor1.execute("select * from time_zone limit 1;")
    record1 = cursor1.fetchone()
    print(record1)
    #print(result1)
    mydb1.commit()
    
    cursor2 = mydb2.cursor()
    result2 = cursor2.execute("select * from ENGINES where transactions = 'YES';")
    record2 = cursor2.fetchone()
    print(record2)
    #print(result2)
    mydb2.commit()
    
    cursor3 = mydb3.cursor()
    #result3 = cursor3.execute("SHOW GLOBAL VARIABLES LIKE 'perf%events%stage%hist%long%';")
    result3 = cursor3.execute("select * from sys_config limit 1;")
    record3 = cursor3.fetchone()
    print(record3)
    #print(result3)
    mydb3.commit()
