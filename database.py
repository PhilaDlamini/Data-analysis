'''Saving data to a database'''
import mysql.connector;

#Saving this code here for reference. However, it is untested -- so test it!!

class Database:
    
    def __init__(self):
        self.conn = mysql.connector.connect(database = 'mybd', user = 'root',
                                            password = 'Coding20', host = 'localhost');
        self.cursor = self.conn.cursor();
    
    def add(self): #The values to be added should be supplied
        try:
            self.cursor.execute("insert into emp values(1, 'Jhn', 2323)");
            self.conn.commit();
        except:
            self.conn.rollback();
        
        self.cursor.close();
        self.conn.close();
    
    def delete(self, id):
        try:
            self.cursor.execute('delete from emp where id = %d'%d);
            self.conn.commit();
        except:
            self.conn.rollback();
        
        self.cursor.close();
        self.conn.close();
        
    def displayData(self):
        self.cursor.execute('select * from emp');
        rows = self.cursor.fetchall();
            
        for row in rows:
            print(row);
        
        self.cursor.close();
        self.conn.close();    
 #Test this code!!!
    
    