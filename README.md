# log_reader for unusual request's
Reading log file and search for unnormal Requests in LOG file and IP's(also check cidr of asn for finding other ip related to unnormal detected ip) 
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ipaddr & ipwhois.

```bash
pip install ipaddr
```
```bash
pip install ipwhois
```
## Usage

```python

#'Change regex_keyword for finding keyword in every line of file '
regex_keyword='(?i)union' #dont change (?i) , its for not mentioning case sensitive in log file.just change union to everything u want.
logfile = 'apache.log' # address of file
```
