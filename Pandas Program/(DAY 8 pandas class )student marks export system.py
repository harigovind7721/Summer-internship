import pandas as pd 
data={
    'Stuent_id':[101, 102, 103, 104, 105,106],
    'Name':     ['Asha', 'Ravi', 'Kiran', 'Meera', 'John','amal'],
    'Subject':  ['math','science','physics','chemistry','biology','psychology'],
    'Marks':    [60,55,90,75,69,44]
}
df=pd.DataFrame(data)
df.to_csv("Studentss.csv",index=False,encoding="utf-8")
print("Student.csv saved successfully..!!!")

df.to_excel("Studentss.xlsx",sheet_name="Marks_Report",index=False)
print("Students.xlxs saved successfully...!!!")

df.to_json("Studentss.json",index=False)
print("Studentss.json saved successfully...!!!!")