import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql

db=pd.read_sql_query("select * from movie",pymysql.connect(host="Localhost", user='anjali',passwd='test', database='project'))

df=pd.DataFrame(db)
print(df)
movdf=df.loc[0:10,"mname"]
boxdf=df.loc[0:10,"mboxoffice"]

name=["Movie names"]
collection=["Collection from movie"]


plt.plot(movdf,boxdf,marker=".",ms=15,mec="b",mfc="r")
plt.plot(movdf,boxdf,color="green")
plt.xlabel("Movie name")
plt.ylabel("Box office collection")
plt.xticks(rotation=75)
plt.legend(collection,loc="lower right",title="Record")
plt.title("Total collection record")
plt.show()


plt.scatter(movdf,boxdf,color="black")
plt.xlabel("Movie name")
plt.ylabel("Box office collection")
plt.xticks(rotation=75)
plt.legend(collection,loc="upper left",title="Record")
plt.title("Collection for oct 2021")
plt.show()



#plt.bar(boxdf,movdf,color="red",width=0.3)
plt.bar(movdf,boxdf,color="blue")
plt.xlabel("Movie name")
plt.ylabel("Box office collection")
plt.xticks(rotation=75)
plt.legend(collection,loc="upper left",title="Record")
plt.title("Highest collection of the movie")
plt.show()


#histogram used to show frequency of data
data=df.loc[0:10,"mboxoffice"]
plt.hist(data,color="cyan")
plt.title("Movie records")
plt.show()



