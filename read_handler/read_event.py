import mysql.connector
#import connect_db
from read_handler.connect_db import MySqlConn
#from connect_db1 import MySqlConn_1

a=10



class read_sql:

  def get_data(self,query):
    self.mysqlConnObj = MySqlConn()
    mysqlConnector = self.mysqlConnObj.mysql_conn
    cursor = mysqlConnector.cursor()
    #cursor.execute("select pod_id,msg,acitvity_time from pod_activities;")
    cursor.execute(query)
    l = []
    for d in cursor:
	    l.append(d)
    return l

  def prepare_query(self,arg1,arg2,arg3):
    print("Beginig")
    QUERY_WHERE_STR = "where"
    QUERY_POD_ID = " pod_id="+arg1
    QUERY_TIME_LIMITS = " acitvity_time>"+arg2+" and acitvity_time<"+arg3+";"
    conditionl_query = ''
    if len(arg1) == 0:
      conditionl_query = QUERY_WHERE_STR + QUERY_TIME_LIMITS
    else:
      conditionl_query = QUERY_WHERE_STR + QUERY_POD_ID + QUERY_TIME_LIMITS
    final_query = "select pod_id,msg,acitvity_time from pod_activities "+ conditionl_query
    #final_query = "select pod_id,msg,acitvity_time from pod_activities;"
    print("Final Query:  ",final_query)
    return final_query


    


