# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:26:31 2018

@author: Pankaj
"""

import sqlite3

conn=sqlite3.connect('usersdatabase.db')

c=conn.cursor()

sql="""
    DROP TABLE IF EXISTS users;
    CREATE TABLE users (
            id integer unique primary key autoincrement,
            name text);
    """
    
c.executescript(sql)

conn.commit()

conn.close()