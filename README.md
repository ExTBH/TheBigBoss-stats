# TheBigBoss-stats

## requirements

- Python >=3.5 or something idk

- BeautifulSoup

- Requests
## Installation
```bash
pip3 install git+https://github.com/ExTBH/TheBigBoss-stats.git@main
```
#### If you get `error: invalid command 'bdist_wheel'`,
#### run the below it should work, idk why just download.
```bash
pip3 install wheel
```
## How to use

```python
Import tbbScraper

```

```python
StatsManager = tbbScraper.Stats()
```

```python
                                #tweak, version(x.y) or (x.y.z), downloads
StatsManager.statsForDev() # -> List[[str, str, int]] <- It's a List of Lists
                           # or False if nothing found.
```
