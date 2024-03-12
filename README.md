# Sfind Subdomain Scan v7.0.0

:heavy_check_mark: Fast :heavy_check_mark: Easy :heavy_check_mark: Modular

**Sfindpy** is a portable and modular `python3` tool designed to quickly enumerate subdomains on a target domain through *passive reconnaissance* and *dictionary scan*.

![sfindpy7](https://github.com/atasky/sfind/assets/41558/b168f105-720f-4f21-aba1-5be5c0326957)

## Install via pip

```
pip install git+https://github.com/atasky/sfind.git
```

## Install via pip requirements.txt file

```
sfindpy @ git+https://github.com/atasky/sfind.git
```

## Install via git

```bash
git clone https://github.com/atasky/sfind.git
cd sfind
pip install .
```

## Usage

```
usage: SFINDPY [-h] [-d DOMAIN] [-f FILE] [-v] [--dns DNS] [--useragent USERAGENT]
               [--timeout TIMEOUT] [--threads THREADS] [--recon] [--bruteforce] 
               [--wordlist WORDLIST] [--json-output] [--list] [--report REPORT]

sfindpy v.7.0.0 - Subdomain Scan
https://github.com/atasky/sfind

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        domain to analyze
  -f FILE, --file FILE  domain list from file path
  -v, --version         show program's version number and exit
  --dns DNS             custom dns
  --useragent USERAGENT
                        custom useragent
  --timeout TIMEOUT     custom timeout
  --threads THREADS     custom threads
  --recon               subdomain reconnaissance
  --bruteforce          subdomain bruteforce
  --wordlist WORDLIST   wordlist file to import
                        --bruteforce option required
  --json                shows output in json format
  --save FOLDER         folder to save report
  --report REPORT       shows saved report
```

### Example

- Start scanning domain with `--recon` and `--bruteforce` options

```bash
sfindpy -d domain.com --recon --bruteforce
```

- Save the report in a folder

```bash
sfindpy -d domain.com --recon --bruteforce --save report
```

- Shows saved report

```bash
sfindpy --report domain.com_yyyy_aa_dd_hh_mm_ss.json
```

### Import as module

```python
from sfind import SFINDPY

domain = 'domain.com'

results = SFINDPY(domain, dns=None, useragent=None, timeout=None, threads=None, recon=True, bruteforce=True, wordlist=None)

print (results)
```
