for (( i = 0; i < 5; i++ )); do
	curl -H "Accept: application/json" -X PUT --data '{"on":false}' http://192.168.0.100/api/newdeveloper/groups/0/action
	sleep 0.25
	curl -H "Accept: application/json" -X PUT --data '{"on":true}' http://192.168.0.100/api/newdeveloper/groups/0/action
done
