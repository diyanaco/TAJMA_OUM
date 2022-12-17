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
- Generate password for counselor@demo.com
  ``` 
  python bcrypt_generator.py
  ```
- Insert hashed_password in sql script for admin@demi.com
- Run __insert-init.sql__
- Run __insert-init2.sql__
