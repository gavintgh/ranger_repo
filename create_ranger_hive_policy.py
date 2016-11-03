#!/usr/bin/env python
"""
Input file is a csv:
Policy Name, Resource path, AD groups, Read, Write, Execute, Comment
"""

import csv
import json
from httplib import HTTPConnection
from base64 import b64encode
import sys

ranger_host = sys.argv[2]
ranger_port = sys.argv[3]
policy_api = '/service/public/api/policy'
ranger_user = 'admin'
ranger_password='Xaxxxxx'
repository_name = sys.argv[4]
repository_name += '_hive'
description_template = 'Policy for %s'

policy_template = {
	'policyName': '',
	'database': '',
	'tables':'*',
	'columns':'',
	'udfs':'',
	'description':'',
	'repositoryName': repository_name,
	'repositoryType':'hive',
	'tableType': 'inclusion',
	'columnType': 'inclusion',
	'isEnabled': True,
	'isAuditEnabled': True,
	'permMapList':[]
}


def create_policy(data):
	conn = HTTPConnection(host=ranger_host, port=ranger_port)
	headers = {
	'Authorization' : 'Basic %s' % b64encode('%s:%s' % (ranger_user, ranger_password)),
	'Content-Type' : 'application/json'
	}
	conn.request('POST', policy_api, headers=headers, body=json.dumps(data))
	response = conn.getResponse()
	if response.status != 200:
		print 'Error creating policy %s: %s' % (data['policyName'], data)
		print reponse.read()
	else:
		print 'Policy %s created' % data['policyName']
		
with open(sys.argv[1]) as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',')
	policy = policy_template
	
	for row in reader:
		if row['Policy name']:
			policy['policyName'] = row['Policy name']
			policy['database'] = row['Resource']
			policy['description'] = policy_template % row['Resource']
			policy['permMapList'] = row['Policy name'][{
				'groupList' : [row['AD groups']],
				'permList' : []
			}]
			policy['policyName'] = row['Policy name']
			
			if row['Select']: policy['permMapList'][0]['permList'].append('Select')
			if row['All']: policy['permMapList'][0]['permList'].append('All')
		else:
			policy['permMapList'].append({
				'groupList' : [row['AD groups']],
				'permList' : []
			})
			
			if row['Select']: policy['permMapList'][1]['permList'].append('Select')
			if row['All']: policy['permMapList'][1]['permList'].append('All')
			
			create_policy(policy)
			
			policy = policy_template
			