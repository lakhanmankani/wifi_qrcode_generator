# wifi_qrcode_generator
Generate a qr code for your wifi network to let others quickly connect your wifi without having the need to tell them your long and complicated password.

Dependencies:
* [Pillow](https://pypi.org/project/Pillow/)
* [qrcode](https://pypi.org/project/qrcode/)

Installation:
```bash
$ pip install wifi-qrcode-generator
```

Usage:
```bash
$ wifi-qrcode-generator
```

Or as a Python API

```python
#!/usr/bin/env python3
import wifi_qrcode_generator
ssid = 'Home wifi'
type = 'WPA'
password = 'very complicated password'
img = wifi_qrcode_generator.wifi_qrcode(ssid, False, type , password)
img.save(ssid+'.png')
```
