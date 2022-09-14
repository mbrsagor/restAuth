# restAuth

> Django authentication system backend API.

#### Setup

##### Dependencies

- Python 3.8
- postgres  12.5

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop 
on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

#### Table of content:
- User Sign Up
- User Sign Up with Activate
- User Sign In
- Rest password with mail
- Change Password
- Profile & Update Profile

All of API already added postman collection. Please check and download.


###### 1st open in your system terminal then follow the command line.

```bash
git clone https://github.com/mbrsagor/restAuth.git
cd restAuth
```

###### Then copy code from the ``env_example`` and create new file `.env` then pasts

-------------------------------------------
```bash
|--> env_example
|--> .env
```


Run the application in your local development server:

```bash
virtualenv venv --python=python3.10
source venv/bin/activate
pip install -r requirements.txt
./manage.py makemigrations accounts
./manage.py migrate
./mangae.py runserver
```


## Happy coding :wink:
