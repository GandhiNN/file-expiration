# File Expiration
Accepts a configuration file written in JSON format as expiration parameters.  
  
Available params:
* name
* path_to_dir
* retention hour
  
**Example usage**  
`python3 expiry.py --config expire.json`
  
**Automate using cronjob**  
`0 * * * * /usr/bin/timeout 300 /bin/expire.py --config /bin/expire.json`

## License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
