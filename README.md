# ONEPasswordToPass

Back up your [1password](https://1password.com/) items to [Pass](https://www.passwordstore.org/)

1Password is awesome, doubly so when sharing passwords with a team,
spouse, or significant other.  Your passwords are stored and shared
securely and available on all your devices.

Pass is pretty awesome too: command line access with passwords stored
in git and GPG encrypted.

1Password now offers a command line client, so why bother with pass?
Two things interest me:

- I like pass's interface and capabilities
- I like having a secure backup of all the data in my 1password account

If that sounds interesting, keep reading.

## First time setup

Download the 1password client:

https://1password.com/downloads/command-line/

Login to 1password:

```
op signin yoursubdomain your@email.com A3-YOURXX-SECRET-KEYXX-XXXXX-XXXXX-XXXXX
```

Install pass:

https://www.passwordstore.org/

Initialize the pass store:

```
$ pass init -p 1password YOUR_KEY_ID

```

Install this program:

```
git clone
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```


## Run the process

```
eval (op signin yoursubdomain)
. ./venv/bin/activate
python onepasswordtopass.py
```
