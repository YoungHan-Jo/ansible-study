#!/usr/bin/env python

import json

def get_inventory_data():
    return {
            "server1": {
                "hosts": ["target1"],
                "vars": {
                    "ansible_user": "ec2-user",
                    "ansible_ssh_private_key_file": "/home/ec2-user/keypair/ansible_key.pem",
                    "ansible_ssh_host": "18.181.244.254"
                    }
                },
            "server2": {
                "hosts": ["target2"],
                "vars": {
                    "ansible_user": "ec2-user",
                    "ansible_ssh_private_key_file": "/home/ec2-user/keypair/ansible_key.pem",
                    "ansible_ssh_host": "54.199.218.230"
                    }
                }
            }

# Default main function
if __name__ == '__main__':
    inventory_data = get_inventory_data()
    print(json.dumps(inventory_data))
