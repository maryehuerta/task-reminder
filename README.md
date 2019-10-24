# task-reminder
smol python program created with the purpose of being over engineered also it creates a todo list

### Todo
 - [X] throw the whole thing in a jenkins pipeline
 - [X] set up pytest
 - [X] use applescript for the todo list reminders
 - [ ] throw the whole program in a docker container when building and testing in jenkins too
 - [ ] use pytest to test in jenkins
 - [ ] Post build action slackbot (because why not i guess)
 - [ ] create more unit tests
 - [ ] Rebuild the whole thing into a website with minimal design but too many animations
 - [ ] Create website that explains what the todo list app does without using the word "todo list"
 - [ ] make the .txt file be a database (why did I think txt was a good idea)
 - [ ] Now fix everything you wrote using "Clean Code"
 - [ ] Find pdf of "clean code"
 - [ ] finish the tiny python program v0
 - [ ] just aws i don't know where but somehow
 
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
