import json

sampleJson2= '''{
  "student": [
    {
      "name": "Sri",
      "rollno": 1345,
      "marks": {
        "Physics": 56,
        "Chemistiry": 70
      }
    },
    {
      "name": "Srini",
      "rollno": 13451,
      "marks": {
        "Physics": 56,
        "Chemistiry": 70
      }
    }
  ]
}'''
sampleDict2= json.loads(sampleJson2)
print(sampleDict2)
print(type(sampleDict2))
'''
for student in sampleDict2['student']:
    
        print(student['name'])
        print(student['rollno'])
        print(student['marks'])
        
'''

for item in sampleDict2['student']['marks']:
    name=item['student']
if 'student' in sampleDict2:
    for i in sampleDict2:
        c1=i
        #s=sampleDict2['student']['marks'][i]
        print(sampleDict2['student(i)']['name(i)'])
        #print(sampleDict2['student']['marks'][i])
        print (c1)
        #print (s)
'''
for key in sampleDict2:
    print(key,sampleDict2[key])
    
