# exl_feed_ctl
1.	Create a python automation: exl_feed_ctl.py and put it in gitlab/github project called exl_feed_ctl
2.	Set the following arguments:
-	list <field name>
List the value of all the parameters with the <field name>
For example:
exl_feed_ctl.py list title
output:
gj
dfg
TEst Video

-	set <id> <field name> <field value>
set a field value for a specific feed ID
for example:
exl_feed_ctl.py set 2138 title "great title"
#exl_json_to_yml
  will pass the json file on the give url to yaml in stdout
