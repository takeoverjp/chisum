# What is Chisum?
Count HIstory SUMmarizer.

Record the following count data (`uniq -c`, `wc -l`) into database with timestamp, and summarise its history.

```
      4 /usr/share/code/libEGL.so
      4 /usr/share/code/libGLESv2.so
     52 /usr/share/code/libffmpeg.so
```

# Howto Setup (for User)

```
pip3 install --user pipenv
pipenv install
```

# Howto Setup (for Developer)

```
pip3 install --user pipenv
pipenv install --dev
```

# Howto Record

```
pipenv run chisum record testdata/counts0.txt out.db test_table
```

# Precommit check

```
pipenv run format && pipenv run lint && pipenv run test
```

# ToDo items

- [ ] Support report
- [ ] Add InMemoryCountRepository
- [ ] Add CsvCountRepository
- [ ] Add class diagram
- [ ] Add ARCHITECTURE.md
