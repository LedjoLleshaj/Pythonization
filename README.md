## Walkthrough of all the exercises in the course

### Check all the chapters in the repository

PS: Some are completely my own, some are from the course, some are from the course and I have modified them.

### How to execute the files

```
python3 <filename>.py
```

### Run your unit tests Poker project

```
#It will run all the tests in the tests folder
python3 -m unittest discover tests
```

### Disclaimer on the Poker project

```
It is not a complete implementation of the poker game, it is just a simple implementation of the game logic.
Mainly to practise the TDD approach and the use of the knowledge acquired in the course.
```

### Start Scrapy project

```
scrapy startproject <project_name>
```

### Start Scrapy shell

```
scrapy shell <url>
```

### Start Scrapy crawl and output to a file

```
scrapy crawl <spider_name> -o <output_file_name>.json
```

### Activate virtual environment

```
source .venv/bin/activate
```

### Save dependencies to requirements.txt

```
pip freeze > requirements.txt
```
