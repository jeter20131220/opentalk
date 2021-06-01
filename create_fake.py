
import dataset
import datetime

db = dataset.connect('mysql://choozmo:pAssw0rd@db.ptt.cx:3306/cmm_test?charset=utf8mb4')
news_table = db['tag_table']
print(type(news_table))
#for idx in range(5):
    #news_table.insert({'name':'標籤'+str(idx),'remark':'remark'+str(idx)})

table = db.load_table('tag_table')
statement = 'SELECT id,name FROM tag_table'
for row in db.query(statement):
    print(row['name'], row['id'])
    


