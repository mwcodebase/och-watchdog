# och-watchdog
Python app that sends out notifications every time a new property is added to University of Maryland's Off Campus Housing (OCH) database that meets defined criteria.

This app was created, tested, and used in Spring of 2020. If/when OCH updates their website there is no gaurantee the app will continue to work.

## Installation/setup

Step 1, as always, is to clone the repo to your machine.

run
```shell
git clone https://github.com/mwcodebase/och-watchdog.git
```
wherever you would like to store the repo.

The main requirement for running this app is to have selenium setup. If you do not already have selenium setup for Python, the documentation can be found here: https://selenium-python.readthedocs.io/

This app's selenium setup utilizes Mozilla Firefox, driven by geckodriver: https://github.com/mozilla/geckodriver

This app also requires several pip packages. To install them, simply run
```shell
pip3 install -r app/requirements.txt
```
from the repo's base directory.

Your setup is now complete, simply run
```shell
python3 app/app.py
```
from the repo's base directory.

## Sending emails

This app's default functionality is to print results to stdout. If you would like to send emails you will need to create a `credentials.env` file in the `app` directory. `credentials.env` should contain this information, verbatim.

```text
recipient_email_address
sender_email_address
sender_email_password
```

The sender's email will need to allow less secure access to the account. An explanation on how to set this up can be found here: https://support.google.com/accounts/answer/6010255?hl=en

Notice, the .gitignore file contains `*.env`. While this is not the most elegant solution to avoiding plaintext password leaks, it suffices for a simple app such as this. That being said, in an abundance of caution, please do not use your main GMail account to send emails with this app. Using a seperate account is also receommended due to the requirement of less secure access to the account (above).
