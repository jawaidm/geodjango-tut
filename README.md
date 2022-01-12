Postgres Notes
--------------
"Create New DB"
sudo -u postgres psql -p 5432
 
CREATE ROLE geo WITH PASSWORD 'geo123' SUPERUSER;
 
ALTER ROLE geo LOGIN;
 
ALTER ROLE geo PASSWORD 'geo123';
 
create database geo_dev; "OR (drop database geo_dev;)"
create exension postgis;
 
"Connect to new DB"
psql -U geo -W -h localhost -d geo_dev -p 5432

_
----------------------------------------------

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

