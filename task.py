import json
import requests
URL=requests.get("http://saral.navgurukul.org/api/courses")
request=URL.json()
with open("requestfile.json","w") as a:
    json.dump(request,a,indent=4)
i=0
id=[]
while i<len(request["availableCourses"]):
    Name=request["availableCourses"][i]["name"]
    Id=request["availableCourses"][i]["id"]
    id.append(Id)
    print(i," ",Name," ",Id)
    i=i+1
choose=int(input("enter the number:"))
r=0
k=requests.get("http://saral.navgurukul.org/api/courses/"+id[choose]+"/exercises")
m=k.json()
list2=[]
for i in m["data"]:
    print(r,i["slug"])
    list2.append(i["slug"])
    r=r+1
choose2=int(input("enter the slug number"))
n=requests.get("http://saral.navgurukul.org/api/courses/"+str(choose)+"exercises/getbyslug?slug="+list2[choose2])
o=n.json()
print(o)