# Soupson Time

Few web scrapers which print weekly menu for [Marche Soupson](http://www.soupson.ca/?lang=en).

# Python

You need to have [`requests`](http://docs.python-requests.org/en/master/) and [`Beautiful soup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) installed:

```sh
$ apt-get install python-requests
$ apt-get install python-bs4
```

The menu could be printed to the output:

```sh
$ python soupson.py <fr or eng>
Monday: Beet and Fennel
Tuesday: Sweet Potato and Lentil
Wednesday: Classic Split Pea Soup
Thursday: Green Vegetable Medley
Friday: HARIRA!
```

or to the file by providing file name as an option:

```bash
$ python soupson.py <fr or eng> menu
$ cat menu
Monday: Beet and Fennel
Tuesday: Sweet Potato and Lentil
Wednesday: Classic Split Pea Soup
Thursday: Green Vegetable Medley
Friday: HARIRA!
```
