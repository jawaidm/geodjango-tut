/*
sudo -u postgres psql -p 5432 -f init.sql
*/

CREATE ROLE geo WITH PASSWORD 'geo123' SUPERUSER;

ALTER ROLE geo LOGIN;

ALTER ROLE geo PASSWORD 'geo123';

create database geo_dev; /* OR (drop database geo_dev;) */
create extension postgis;

/*
"Connect to new DB"
psql -U geo -W -h localhost -d geo_dev -p 5432
*/
