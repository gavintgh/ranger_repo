import json

input_file=open('/tmp/gavin/gavin.hdfs.out')
output_file=open('/tmp/gavin/ranger.hdfs.out')

policy_template = {
   'name': '',
   'policyItems': [],
   'path': []
   }

item = json.load(input_file)

result = item['policies']

for i in range(len(result)):
   policy = policy_template
   policy['name'] = result[i]['name']
   
   policy['policyItems'] = [{
      'users':[],
	  'groups':[],
	  'accesses':[]
   }]
   policy['path'] = [{
      'values':[]
   }]
   if result[i]['policyItems']:
      for k in range(len(result[i]['policyItems'])):
	     if result[i]['policyItems'][k]['groups']:
		    for j in range(len(result[i]['policyItems'][k]['groups'])):
			   policy['policyItems'][0]['groups'].append(result[i]['policyItems'][k]['groups'][j])
		 if result[i]['policyItems'][k]['users']:
		    for j in range(len(result[i]['policyItems'][k]['users'])):
			   policy['policyItems'][0]['users'].append(result[i]['policyItems'][k]['users'][j])
		 if result[i]['policyItems'][k]['accesses']:
		    for j in range(len(result[i]['policyItems'][k]['accesses'])):
			   policy['policyItems'][0]['accesses'].append(result[i]['policyItems'][k]['accesses'][j]['type'])
		 	   
   if result[i]['resources']:
      if result[i]['resources']['path']:
	     for k in range(len(result[i]['resources']['path']['values'])):
		    policy['path'][0]['values'].append(result[i]['resources']['path']['values'][j])
	
	back_json = json.dumps(policy,output_file)
	output_file.write(back_json + '\n')
	
input_file.close()
output_file.close()

   
