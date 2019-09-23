import base36 
import base65536

import base62
import base91
import base58
import argparse
import base64

parse=argparse.ArgumentParser()
parse.add_argument('-s',help='input a encode string',type=str,default='1ewy')
parse.add_argument('-b128',help='base128',type=list,default=[b'0\x01', [1]])
all_decode=[base64.b64decode,
     base64.b16decode,
     base64.b32decode,
     base64.b85decode,
     base64.a85decode,
     base58.b58decode,
     base62.decode,
     base36.dumps,
     base91.decode,
     base65536.decode
     ]
all_name=['base64','base16','base32','base85','a85','base58','base62','base36','base91','base65536']
args=parse.parse_args()
def base(string):
    for i in range(len(all_decode)):
        try:
            decode=all_decode[i](string)
            print('[*] {} is ok -->'.format(all_name[i]))
            print(decode)
        except:
            print('can not {}'.format(all_name[i]))

base(args.s)

