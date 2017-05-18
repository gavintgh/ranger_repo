# ranger_repo
This ranger repo introduce two python script to update ranger policy for hdfs and hive. Also the sample hdfs/hive csv template so we can batch update ranger policy.

Instruction
-----------------------------------------------------------------------------------------------------------------------------------------------------------
python create_ranger_hdfs_policies.py <hdfs_ranger_csv> <ranger server> <ranger port> <prefix of ranger repository>
python create_ranger_hive_policies.py <hive_ranger_csv> <ranger server> <ranger port> <prefix of ranger repository>

Output
---------------------------------------------------------------------------------------------------------------------------------------------------------
Policy xxxxxxx Created


Added two more python scripts for policy extraction from ranger, this is useful when doing migration:

1, Retrieve json policy from ranger

2, Extract specific policy detail from json

