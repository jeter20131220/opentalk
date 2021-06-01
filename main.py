
from enum import Enum
from typing import Optional

from fastapi import FastAPI, Query
import dataset,json


app = FastAPI()
db = dataset.connect('mysql://choozmo:pAssw0rd@db.ptt.cx:3306/cmm_test?charset=utf8mb4')

@app.get("/tags")
async def get_tags():
    tag_dict = {}
    table = db.load_table('tag_table')
    statement = 'SELECT id,name FROM tag_table'
    for row in db.query(statement):
        tag_dict[row['id']]=row['name']
        json_dump = json.dumps(tag_dict, ensure_ascii=False)
    
    return json_dump


