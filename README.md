# What is TSDraw?

Time Series Drawer.

Import the following syle data (`uniq -c`) into database with timestamp, and summarise its time series.

```
      4 /usr/share/code/libEGL.so
      4 /usr/share/code/libGLESv2.so
     52 /usr/share/code/libffmpeg.so
```

# Howto Setup

```
pip3 install --user pipenv
pipenv install
```

# Precommit check

```
pipenv run format && pipenv run lint && pipenv run test
```