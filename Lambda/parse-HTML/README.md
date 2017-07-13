# parse HTML lambda

Lambda function that takes a PUT request with a url string. Parses the HTML of that url and returns as the following json object with exracted HTML content.

```json
{
"text": "...",
"image": "...",
"authors": [..., ...],
"title": "..."
}
```