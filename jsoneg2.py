#!/usr/bin/python
import json
import sqlite3

sampleJson2= '''{
  "student": [
    {
      "rollno": 12,
      "name": "Sri",
      "mark1": 85,
      "mark2": 90,
      "mark3": 89
    },
    {
      "rollno": 34,
      "name": "Vas",
      "mark1": 78,
      "mark2": 87,
      "mark3": 94      
    }
  ]
}'''


conn = sqlite3.connect('check.db')
print ("Opened database successfully")

cur = conn.cursor()

# check if table exists
print('Check if STUDENT table exists in the database:')
cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='STUDENT9' ''')
#if the count is 1, then table exists
if cur.fetchone()[0]==1 : {
	print('Table exists.')
}
else:{
    conn.execute('''CREATE TABLE STUDENT10
        (ROLLNO         INT      NOT NULL,
         NAME           TEXT     NOT NULL,
         MARK1          INT,
         MARK2          INT,
         MARK3          INT);''')
       }


sampleDict2= json.loads(sampleJson2)
print(sampleDict2)
print(type(sampleDict2))

columns = ', '.join(sampleDict2.keys())
print(columns)
print(len(sampleDict2))
placeholders = ', '.join('?' * len(sampleDict2))
print(placeholders)
sql = 'INSERT INTO STUDENT10 ({}) VALUES ({})'.format(columns, placeholders)
print(sql)
values = [int(x) if isinstance(x, bool) else x for x in sampleDict2.values()]
print(values)
cur.execute(sql, values)

'''
for student in sampleDict2['student']:
    
        #print(student['name'])
        name=student['name']
        print(str(name))
        
        c1=student['rollno']
        s1=int(c1)
        print(s1)
        print(int(c1))
        
        c2=student['mark1']
        s2=int(c2)
        print(s2)
        print(int(c2))
        c3=student['mark2']
        s3=int(c3)
        print(s3)
        print(int(c3))
        print(int(c3))
        c4=student['mark3']
        s4=int(c4)
        print(s4)
        print(int(c4))
        
        
        conn.execute("INSERT INTO STUDENT9 (ROLLNO,NAME,MARK1,MARK2,MARK3) \
                      VALUES (s1,'name',s2,s3, s4)");
                    
        conn.commit()
        
        print ("Records created successfully")
'''

        
       
