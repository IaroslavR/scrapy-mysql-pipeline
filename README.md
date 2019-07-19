![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)  

## scrapy-mysql-pipeline  
Asynchronous mysql [Scrapy](https://doc.scrapy.org/en/latest/) item pipeline  

#### Installation  
```bash
pip install scrapy-mysql-pipeline
```
#### Configuration  
Add pipeline  
```python
ITEM_PIPELINES = {
    'scrapy_mysql_pipeline.MySQLPipeline': 300,
}
```
Default values:  
```python
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = None
MYSQL_PASSWORD = ''
MYSQL_DB = None
MYSQL_TABLE = None
MYSQL_UPSERT = False
MYSQL_RETRIES = 3
MYSQL_CLOSE_ON_ERROR = True
MYSQL_CHARSET = 'utf8'
```
`MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DB` and `MYSQL_TABLE`,  variables must be set in settings.py  
