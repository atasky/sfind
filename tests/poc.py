from sfind import SFINDPY

domain = 'github.com'

results = SFINDPY(domain, dns=None, useragent=None, timeout=None, threads=None, recon=True, bruteforce=True, wordlist=None)

print (results)