import sys
from base64 import b64decode

import requests


def get_info(number: str):
    resp = requests.get(
        url="https://akash-rpc.polkachu.com/block",
        params={"height": number}
    )
    if not resp.status_code == 200:
        sys.exit(resp.text)
    data = resp.json()
    txs_list = data["result"]["block"]["data"]["txs"]
    if not txs_list:
        sys.exit("No transactions")
    for txs in txs_list:
        print(f"{'*' * 50}\n{b64decode(txs)}")


if __name__ == '__main__':
    get_info(input("Please, enter block number: "))
