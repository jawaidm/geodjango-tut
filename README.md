# 1. Clone from github  
cd /var/www  
git clone https://github.com/jawaidm/geodjango-tut.git  
cd geodjango-tut 
 
sudo apt install gdal-bin
virtualenv venv  
source venv/bin/activate

pip install -r requirements.txt

# 2. Create Postgres DB  
"Create New DB"  
sudo -u postgres psql -p 5432
 
CREATE ROLE geo WITH PASSWORD 'geo123' SUPERUSER;
 
ALTER ROLE geo LOGIN;
 
ALTER ROLE geo PASSWORD 'geo123';
 
create database geo_dev; "OR (drop database geo_dev;)"

create exension postgis;
 
"Connect to new DB"  
psql -U geo -W -h localhost -d geo_dev -p 5432  


# 3. Create .env file  
DEBUG=True  
DATABASE_URL="postgis://geo:geo123@localhost:5432/geo_dev"  
SECRET_KEY='SECRET_KEY_YO'  
ALLOWED_HOSTS=['*']  
CONSOLE_EMAIL_BACKEND=True  
_

# 4. Run Migrations

./manage.py showmigrations

./manage.py migrate

# 5. Test
ogrinfo world/data/json/dpaw_regions.json  

ogrinfo -so world/data/json/dpaw_regions.json dpaw_regions

./manage.py ogrinspect --name-field region --blank true --null true --layer dpaw_regions --mapping --multi world/data/json/dpaw_regions.json DpawRegion


# 6. Test API EndPoint  
./manage.py runserver 0.0.0.0:8000  
curl -H 'Accept: application/json; indent=4' -u admin:admin123 http://127.0.0.1:8000/dpaw_regions/  

{
    "count": 9,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "http://127.0.0.1:8000/dpaw_regions/1/",
            "feat_id": "dpaw_regions.fid-5df1949a_17e4850579c_-29e",
            "region": "GOLDFIELDS",
            "ogc_fid": 0,
            "office": "KALGOORLIE",
            "hectares": 84251815.4161,
            "md5_rowhash": "c48a563e67d813e5f37191d81c7e7ee1"
        },
        {
            "url": "http://127.0.0.1:8000/dpaw_regions/2/",
            "feat_id": "dpaw_regions.fid-5df1949a_17e4850579c_-29d",
            "region": "KIMBERLEY",
            "ogc_fid": 1,
            "office": "KUNUNURRA",
            "hectares": 46661522.931,
            "md5_rowhash": "f064c1699a9ce4c53464eea6e794585e"
        },
        ....

