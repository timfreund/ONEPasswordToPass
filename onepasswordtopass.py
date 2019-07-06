import json
import random
import subprocess
import time

from slugify import slugify

if __name__ == '__main__':
    proc = subprocess.run("op list vaults".split(" "), capture_output=True)
    raw_vaults = json.loads(proc.stdout)
    vaults = {}
    for rv in raw_vaults:
        rv['slug'] = slugify(rv['name'])
        rv['items'] = []
        vaults[rv['uuid']] = rv

    proc = subprocess.run("op list items".split(" "), capture_output=True)
    raw_items = json.loads(proc.stdout)
    for i in raw_items:
        vaults[i['vaultUuid']]['items'].append(i)

    # import IPython; IPython.embed()
    for v in vaults.values():
        for i in v['items']:
            cmd = "op get item %s" % i['uuid']
            proc = subprocess.run(cmd.split(" "), capture_output=True)
            full_item = json.loads(proc.stdout)
            full_item['slug'] = slugify(i['overview']['title'])

            insert_cmd = "pass insert -m -f 1password/%s/%s" % (v['slug'], full_item['slug'])
            item_json = json.dumps(full_item, indent=2, sort_keys=True)
            print(insert_cmd)
            # print(item_json)
            proc = subprocess.run(insert_cmd.split(" "), input=item_json.encode(), capture_output=True)
            print(proc.stdout.decode())
            # why sleep?  I don't know if 1Password is rate limited and
            # I'd like to stay on their good side since I like their service
            time.sleep(random.randint(5, 30))
