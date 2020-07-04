# Cosmos Website

## Instructions

1. Activate Python virtual environment
```bash
source ./venv/bin/activate
```

2. Install MariaDB
```bash
# Arch Linux
yay -S mariadb mariadb-libs
sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql

# OpenSUSE
sudo zypper install libmariadb-devel

# ALL
sudo systemctl start mariadb
sudo mysql_secure_installation
y, y, <password>, y, y, y, y
```

3. Initialize database

```bash
mysql -u root -p
```

4. Init test database

```bash
mysql -u root -p
source ./init_db.sql
```

4. Install Python dependencies

```bash
pip install -r requirements
```

5. Copy settings.template into settings.py

```bash
cp mysite/settings.template.py mysite/settings.py
```

6. Configure settings.template

7. Run `python manage.py migrate`

Django has a system for migrations to prevent loads of changes, both in the db and backend. This command fixes up the database according to the model in the backend.

8. Run `python manage.py createsuperuser`

This creates an administrator account which is required for creating any sort of content for the CMS.

# Changes

- switch from MySQL to MariaDB (community-developed fork, read Google)
- upgraded from Django 2 to Django 3

# TODO

- use os.path.join
- keep database schema inside of git repository
- maybe require gdal?
