# TAJMA_OUM
Profiling System where students of OUM will take questionaire to determine traits of personality


## Clone repository
- Download github desktop
- Sign in 
- File -> Clone repository
- Enter url https://github.com/ZaimAndTaufiq/TAJMA_OUM.git

## Run system
- Activate virtualenv
```
oum\Scripts\activate
```
- In the visual code terminal 
```
- create .env file
export FLASK_APP='run.py'
flask run
```

- View url in the browser

## Warning
Only commit changes to your branch only (Taufiq)

## Version 3.2
Enhance the questionaire to flow one direction and hardcode the questionaire and answer inside templates
Add role based authentication manually without using packages

## Alembic
alembic revision --autogenerate -m "Added account table"
alembic upgrade head

### to clean the tree, will point to the latest revision created
```
alembic downgrade base
alembic upgrade head
```
### to downgrade revision 
```
alembic upgarade a12
```
### to downgrade
```
alembic stamp <revision>
alembic downgrade -1
```
### point to a revision id
```
alembic stamp a12
```
### Notes 
If want to rename a table, must first create the table model
