[![License](https://img.shields.io/badge/license-MIT-_red.svg)](https://opensource.org/licenses/MIT)
![Follow on Twitter](https://img.shields.io/twitter/follow/Dheerajmadhukar?style=social)

### Updated
Add auto_bypasser.py for targeting multiple urls.
![auto_bypasser result](https://github.com/user-attachments/assets/010d101e-b337-4878-b213-3dc150c936fa)

### >_ Introduction

**4-ZERO-3**
Tool to bypass 403/401. This script contain all the possible techniques to do the same. 

- **NOTE** : If you see multiple [200 Ok]/bypasses as output, you must check the Content-Length. If the content-length is same for multiple [200 Ok]/bypasses means false positive. Reason can be "301/302" or "../" [Payload] DON'T PANIC.
- Script will print `cURL` PAYLOAD if possible bypass found.

### >_ Preview
![4-ZERO-3_priview](https://github.com/Dheerajmadhukar/4-ZERO-3/blob/main/img/4-ZERO-3_priview.gif)

### >_ Help
```bash
root@me_dheeraj:$ bash 403-bypass.sh -h
```
<img src="img/403-help.png" alt="4-ZERO-3" width="1000px">

### >_ Usage / Modes

- Scan with specific payloads:
  * [ `--header` ] Support HEADER based bypasses/payloads
    ```bash
    root@me_dheeraj:$ bash 403-bypass.sh -u https://target.com/secret --header
    ```
  * [ `--protocol` ] Support PROTOCOL based bypasses/payloads
    ```bash
    root@me_dheeraj:$ bash 403-bypass.sh -u https://target.com/secret --protocol
    ```
  * [ `--port` ] Support PORT based bypasses/payloads
    ```bash
    root@me_dheeraj:$ bash 403-bypass.sh -u https://target.com/secret --port
    ```
  * [ `--HTTPmethod` ] Support HTTP Method based bypasses/payloads
    ```bash
    root@me_dheeraj:$ bash 403-bypass.sh -u https://target.com/secret --HTTPmethod
    ```
  * [ `--encode` ] Support URL Encoded bypasses/payloads
    ```bash
    root@me_dheeraj:$ bash 403-bypass.sh -u https://target.com/secret --encode
    ```
  * [ `--SQLi` ] Support MySQL mod_Security & libinjection bypasses/payloads [** New **]
    ```bash
    root@me_dheeraj:$ bash 403-bypass.sh -u https://target.com/secret --SQLi
    ```
- Complete Scan {includes all exploits/payloads} for an endpoint [ --exploit ]
```bash
root@me_dheeraj:$ bash 403-bypass.sh -u https://target.com/secret --exploit
```

##### Prerequisites
- apt install curl [Debian]
