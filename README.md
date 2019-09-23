# base
base.py
需要
pip3 install -r requirement.txt
```
用法python3 base.py -s '字符串'
```
python3
可以解的是
*base16
*base32
*base36
*base62
*base58
*base64
*base85
*a85
*base91
*base65536

本来找了个base128的
结果base128需要的格式很奇怪
需要这样的格式 [b'0\x01', [1]]
第一个是要字节形式
还有个base116676的又是奇怪的不弄了
那就不弄了


base92也找到了，不过要python2
需要pip install base92
在base92_py2.py
用法
python2 base92_py2.py -s '字符串'
