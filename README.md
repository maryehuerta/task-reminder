# task-reminder
smol python program created with the purpose of being over engineered also it create a todo list

### Todo
 - [ ] create more unit tests
 - [ ] use applescript for the todo list reminders
 - [ ] actually finish the tiny python program
## Running Reminders
`python PyRemind.py`

## Running Tests
`python -m pytest tests/`

## Running Jenkins in Docker
kind of unrelated
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

note: no scan repository triggers for now go to the project in jenkins and click `Scan Repository Now`