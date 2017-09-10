from xmlutils.xml2json import xml2json
import json
f= open('/home/dell1/Documents/Crayon/actualoutput2')
actual = f.read()
splitted=actual.split('------------------')
#print splitted
final=[]

dict={}
def x(a,b,c,i):
        converter = xml2json(a,b,encoding=c)
	converter.convert()
	f2=open ('/home/dell1/Documents/Crayon/samp'+str(i)+'.json','r')
	finaljson1=f2.read()
	f2.close()
	#print finaljson1
	final.append(finaljson1)
i=0
for splits in splitted :
	
        
    i=i+1
	f1= open('/home/dell1/Documents/Crayon/test'+str(i)+'.xml','w')
	f1.write(splits.strip())
        f1.close
	
for i in range(1,4):
#for i in len(splitted)
  print i
  x('/home/dell1/Documents/Crayon/test'+str(i)+'.xml','samp'+str(i)+'.json','utf-8',i)
	

#print final
#finaljson=json.dumps(final)
#print final
f4= open('/home/dell1/Documents/Crayon/finalout.json','w')
string = "["
for data in final:
	string = string + data + ","
	
string = string[:-1] +"]"
f4.write(string)
f4.close()

