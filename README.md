# OUM Psychometric Test
Profiling System where students of OUM will take questionaire to determine traits of personality

## Run system
- Create venv
```
python -m venv venv
```
- Install libraries
```
pip install -r requirements.text
```

- Run app
```
python run.py
```
- Generate password for admin@demo.com
  ``` 
  python bcrypt_generator.py
  ```
- Insert hashed_password in sql script for admin@demi.com
- Run __insert-init.sql__


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
