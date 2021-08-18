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
pipenv run chisum record testdata/counts1.txt out.db test_table
```

# Howto Report

```
$ pipenv run chisum report out.db test_table
   54 (   -4) TOTAL
-------------------
    1 (   +0) /lib/modules/5.4.0-80-generic/modules.alias.bin
    1 (   +0) /lib/modules/5.4.0-80-generic/modules.dep.bin
   36 (  +10) /lib/systemd/libsystemd-shared-237.so
    5 (  -10) /lib/systemd/systemd
    3 (   +0) /lib/systemd/systemd-journald
    0 (   -3) /lib/systemd/systemd-logind
    3 (   +0) /lib/systemd/systemd-resolved
    0 (   -3) /lib/systemd/systemd-timesyncd
    3 (   +0) /lib/systemd/systemd-udevd
    1 (   +1) /lib/modules/5.4.0-80-generic/modules.builtin.bin
    1 (   +1) /lib/modules/5.4.0-80-generic/modules.symbols.bin
```

# Precommit check

```
pipenv run format && pipenv run lint && pipenv run test
```

# ToDo items

- [ ] Add CsvCountRepository
- [ ] Directoryを分ける
- [ ] Repositoryのunittestをまとめる
- [ ] 相対パスを使ってimport
- [ ] importの並び替え自動化
- [ ] datetimeのutc強制
