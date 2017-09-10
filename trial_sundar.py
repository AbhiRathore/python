from xmlutils.xml2json import xml2json
import json
f= open("D:/triposo/output3")
actual = f.read()
splitted=actual.split('------------------')
#print splitted
final=[]

dict={}
def x(a,b,c,i):
    converter = xml2json(a,b,encoding=c)
    converter.convert()
    f2=open ('D:/triposo/samp2'+str(i)+'.json','r')
    finaljson1=f2.read()
    f2.close()
    #print finaljson1
    final.append(finaljson1)
i=0
for splits in splitted :
    i=i+1
    f1= open('D:/triposo/test2'+str(i)+'.xml','w')
    f1.write(splits.strip())
    f1.close
    
for j in range(1,i):
  print j
  x('D:/triposo/test2'+str(j)+'.xml','D:/triposo/samp2'+str(j)+'.json','utf-8',j)
    

#print final
#finaljson=json.dumps(final)
#print final
f4= open('D:/triposo/finalout4.json','w')
#string = "["
for data in final:
    #string = string + data + ","
	f4.write(json.dumps(json.loads(data)))
	f4.write('\n')
    
#string = string[:-1] +"]"
#f4.write(string)
f4.close()

