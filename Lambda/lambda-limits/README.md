# Pushing the AWS Limits

Can you deploy packages on AWS lambda that are bigger than the 50 MB hard limit?

[ANALYSIS REPORT](https://docs.google.com/document/u/2/d/1trBt1KfTCIZb6hCWNGxI6ryVfr7OxqMQXSc_Y549J7s/pub)

## Step 1 - slim-parse-HTML

Using the Zappa `slim handler`. Slim handler works by uploading larger deployment packages to S3 buckets and then pulling/expanding them to the Lamba `/tmp` directory at run time. I tested this an exisitng parse HTML lambda function

## Step 2 - named-entity-lambda-extract

Attemped to put an even bigger deployment package containing a MITIE named entity extractor behind a Lambda using the already tested slim parse method.