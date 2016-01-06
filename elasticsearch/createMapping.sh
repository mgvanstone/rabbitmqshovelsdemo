curl -XPUT 'http://localhost:9200/rni-test/record/_mapping' -d '{
 "record" : {
 "properties" : {
 "primary_name" : { "type" : "rni_name" },
 "dob" : { "type" : "string" }
 }
 }
}'
