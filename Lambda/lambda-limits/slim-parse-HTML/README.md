# Parse HTML Lambda (slim version)

Took existing `parseHTML` lambda function with API trigger and used [Zappa tool](https://github.com/Miserlou/Zappa) to deploy and test the `50MB` lambda hard limit using the `slim_handler` attribute. 

[.../slim-handler-test](https://eghaw63l3b.execute-api.us-west-1.amazonaws.com/test4)

tested without the original PUT request. Uses static url and test article `"https://static01.nyt.com/images/2017/06/13/us/13partisan-picks-comey/13partisan-picks-comey-facebookJumbo.jpg"`

## slim handler

When `slim_handler` is set `true` in `zappa_settings.json`, zappa executes as follows:
1. Creates two Zip files for S3. The first is a small handler-only zip (apx 5M) that contains the Zappa handler.py file and zappa's dependencies. The second is the application with all of its dependencies
2. Copies the versioned application zip to proj_current_project.zip
3. Adds a ZIP_PATH=proj_current_project.zip line to the zappa_settings.py module that is loaded by the handler
4. When the handler sees the ZIP_PATH= line, it downloads that zip from S3 into /tmp, unzips it, and adds it to path.

