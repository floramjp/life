# lifx
2016.06.13 ver.1 - blink.py documented.
2016.06.14 ver.2 - pull_request.py updated.

This is Flora Park's project using lifx.
Given repo and authentication is substituted as "confidential" in this public source code. Github API is used for development and mclarkk/lifxlan is used for rainbow blinks.
The repo contains the source code for manipulating the wifi-lightbulb (lifx) accordingly to different actions on the repo.

blink.py
*******************************************************************
The python program controls the wifi-lightbulb (lifx) to display all colors of the rainbow when someone commits on the master branch in a given repo.

pull_request.py
*******************************************************************
The python program controls the wifi-lightbulb (lifx) to display blue when there is a pull request in a given repo. The stdout prints the PR number, user login, PR title, and timestamp.


