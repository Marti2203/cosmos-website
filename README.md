# Cosmos Website

## Instructions

1. Activate Python virtual environment

```bash
source venv/bin/activate
```

2. Install MariaDB

```bash
// Arch Linux
yay -S mariadb mariadb-libs

// OpenSUSE
sudo zypper install libmariadb-devel
```


3. Initialize database

```bash
$ mysql_secure_installation
```

4. Init test database

```mysql
CREATE DATABASE cosmos_website_test CHARACTER SET UTF8;
CREATE USER cosmos_website_tester@localhost IDENTIFIED BY '2020123';
GRANT ALL PRIVILEGES ON cosmos_website_test.* TO cosmos_website_tester@localhost;
FLUSH PRIVILEGES;
```

4. Install Python dependencies

```python
pip install -r requirements
```

5. Copy settings.template into settings.py

# Changes

- switch from MySQL to MariaDB (community-developed fork, read Google)

# TODO

- use os.path.join
- keep database schema inside of git repository
- maybe require gdal?
