from dotenv import dotenv_values

import pymysql
import pymysql.cursors

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

config = dotenv_values('.env')

mysql_conn_params = {
        'user': config['MYSQL_USERNAME'],
        'password': config['MYSQL_PASSWORD'],
        'host': 'localhost',
        'database': 'project'
        }

mysql_connection = pymysql.connect(**mysql_conn_params,
                                   cursorclass=pymysql.cursors.DictCursor)
db_cursor = mysql_connection.cursor()

app = FastAPI()

origins = [
            "http://localhost",
            "http://localhost:5173",
            "https://localhost",
            "https://localhost:5173",
            ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root_path():
    return {"ping": "pong"}


@app.get('/ping')
def ping_pong():
    return 'pong'


@app.get('/countries')
def get_countries():
    db_cursor.execute('SELECT country_id, name FROM country')
    data = db_cursor.fetchall()
    data_fmt = [{
        'id': d['country_id'], 'name': d['name']
        } for d in data]
    # print ( data_fmt )
    return data_fmt


@app.get('/countries/{region}')
def get_countries_by_region(region: str):
    sql = '''
    SELECT country_id, country.name FROM country, region
    WHERE country.region_id=region.region_id
    AND TRIM(region.name)=%s
    '''
    db_cursor.execute(sql, [region.lower().replace('_', ' ')])
    data = db_cursor.fetchall()
    data_fmt = [{
        'id': d['country_id'], 'name': d['name']
        } for d in data]
    return data_fmt


@app.get('/regions')
def get_regions():
    db_cursor.execute('SELECT name FROM region')
    data = db_cursor.fetchall()
    data_fmt = [{'name': d['name']} for d in data]
    return data_fmt


@app.get('/suicides')
def get_suicides():
    db_cursor.execute('SELECT country_id, total FROM suicide_rates')
    data = db_cursor.fetchall()
    data_fmt = [{
        'country': d['country_id'], 'score': d['total']
        } for d in data]
    return data_fmt


@app.get('/suicides/{year}')
def get_suicides_by_year(year: int):
    sql = 'SELECT country_id, total FROM suicide_rates WHERE year=%s'
    db_cursor.execute(sql, [year])
    data = db_cursor.fetchall()
    data_fmt = [{
        'country': d['country_id'], 'score': d['total']
        } for d in data]
    return data_fmt


@app.get('/happiness')
def get_happiness():
    db_cursor.execute('SELECT countries_country_id, score FROM happiness')
    data = db_cursor.fetchall()
    data_fmt = [{
        'country': d['countries_country_id'], 'score': d['score']
        } for d in data]
    return data_fmt


@app.get('/happiness/{year}')
def get_happiness_by_year(year: int):
    sql = 'SELECT countries_country_id, score FROM happiness WHERE year=%s'
    db_cursor.execute(sql, [year])
    data = db_cursor.fetchall()
    data_fmt = [{
        'country': d['countries_country_id'], 'score': d['score']
        } for d in data]
    return data_fmt


@app.get('/life-expectancy')
def get_life_expectancy():
    db_cursor.execute(
            'SELECT countries_country_id, expectancy FROM life_expectancy'
            )
    data = db_cursor.fetchall()
    data_fmt = [{
        'country': d['countries_country_id'], 'score': d['expectancy']
        } for d in data]
    return data_fmt


@app.get('/life-expectancy/{year}')
def get_expectancy_by_year(year: int):
    sql = '''
    SELECT countries_country_id, expectancy FROM life_expectancy WHERE year=%s
    '''
    db_cursor.execute(sql, [year])
    data = db_cursor.fetchall()
    data_fmt = [{
        'country': d['countries_country_id'], 'score': d['expectancy']
        } for d in data]
    return data_fmt
