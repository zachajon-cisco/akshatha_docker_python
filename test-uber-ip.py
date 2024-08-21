#!/usr/bin/env python

import boto3
import json
import requests

from aws_requests_auth.aws_auth import AWSRequestsAuth


# This code requires the user to have valid Streamline Credentials stored in .aws/credentials
# To generate valid streamline credentials run the following command
# sl aws session generate --account-id <account_id> --role-name <role_name> --region us-east-1

if __name__ == "__main__":
    # convert text file hash_test.txt to list of hashes
    # with open('hash_test.txt') as f:
    #     hashes = f.read().splitlines()
    # f.close()

    # convert text file ip_test.txt to list of ips
    print("hello")
    with open("ip_test.txt") as f:
        ips = f.read().splitlines()
    f.close()

    # convert text file domain_test.txt to list of domains
    # with open('domain_test.txt') as f:
    #     domains = f.read().splitlines()
    # f.close()

    # create boto3 session using streamline profile
    session = boto3.Session(profile_name="strln")
    creds = session.get_credentials()
    auth = AWSRequestsAuth(
        aws_access_key=creds.access_key,
        aws_secret_access_key=creds.secret_key,
        aws_token=creds.token,
        aws_host="api.dev.thetap.cisco.com",
        aws_region="us-east-1",
        aws_service="execute-api",
    )
    # generate API request for each hash in list
    # for hash in hashes:
    #     uber_hash_url = 'https://api.dev.thetap.cisco.com/uber/v3/hash/e/sha256/' + hash
    #     response = requests.get(uber_hash_url, auth=auth)
    #     print(response.json())

    # generate API request for each ip in list
    for ip in ips:
        uber_ip_url = "https://api.dev.thetap.cisco.com/uber/v3/ip/e/" + ip
        print(response.json())

    # generate API request for each domain in list
    for domain in domains:
        uber_domain_url = "https://api.dev.thetap.cisco.com/uber/v3/domain/e/" + domain
        response = requests.get(uber_domain_url, auth=auth)
        print(response.json())

    # domain_body = {
    #     "domain_string": ["cisco.com", "google.com"],
    #     "index_type": "e"
    # }
    # hash_body = {"hash_string": ["6f000194c4d7a418e569a893c1b522de", "6f0001812ebe7f40bc725b5691bfcaa2"],"hash_type": "sha256","index_type": "e"}
    ip_body = {"ipaddress": ["8.8.8.8", "2607:fdc8:7::17"], "index_type": "e"}
    # uber_domain_post_url = 'https://api.dev.thetap.cisco.com/uber/v3/domain'
    # uber_hash_post_url = 'https://api.dev.thetap.cisco.com/uber/v3/hash'
    uber_ip_post_url = "https://api.dev.thetap.cisco.com/uber/v3/ip"

    # response_post_domain = requests.post(uber_domain_post_url, auth=auth, data=domain_body)
    # print(response_post_domain)

    # response_post_hash = requests.post(uber_hash_post_url, auth=auth, data=hash_body)
    # print(response_post_hash.json())

    response_ip_hash = requests.post(uber_hash_post_url, auth=auth, data=ip_body)
    print(response_post_ip.json())
