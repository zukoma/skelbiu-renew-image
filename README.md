# About
Docker image for Skelbiu.lt renew ads script bundled with Firefox and Geckodriver. Script scheduled on a cronjob for 6pm everyday.

# Usage

```
docker build -t skelbiu_renew .

sudo docker run --name <name> -d -e APP_USERNAME=<username> -e APP_PASSWORD=<password> skelbiu_renew sleep infinite
```
