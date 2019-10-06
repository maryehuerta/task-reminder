# task-reminder

## Running Reminders
`python PyRemind.py`

## Running Tests
`python -m pytest tests/`

## Running Jenkins in Docker

```
sudo docker run \                                         
  -u root \
  --rm \
  -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkinsci/blueocean
  ```
