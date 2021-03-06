# This string will be evaluated by mongo with the --eval flag
eval_string = "db.runCommand( {connectionStatus: 1});"
# All of or a portion of what you expect in the result to be successful
expected_output = "\"ok\" : 1"
# Optional user authentication
username = None
# Optional password authentication
password = None
# Path to mongo executable. *NIX systems often work with just "mongo"
# The r is in place for "raw string" when inserting a Windows path
mongo_path = r"mongo"
