# parse HTML lambda

[https://...amazonaws.com/beta/parseHTML](https://uaeb6qlibd.execute-api.us-west-1.amazonaws.com/beta/parseHTML)

Lambda function that takes a PUT request with a url string. Parses the HTML of that url and returns as the following json object with exracted HTML content.

```json
{
"text": "...",
"image": "...",
"authors": [..., ...],
"title": "..."
}
```