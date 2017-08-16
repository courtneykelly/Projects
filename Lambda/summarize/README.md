# Summarizer Function

This function takes a PUT request with a `url` data object and/or a `sentence count` data object [the default value for sentence count is 5]. It takes the given url, summarizes it, and returns the following json object.


```json
{
"authors": [..., ...],
"summary": "...",
"title": "..."
}
```

[https://amazonaws.com/summarize](https://xo6vn2nhac.execute-api.us-west-1.amazonaws.com/api) 

## Installations

Need to be running on python2.7. There is a problem with `nltk` and python 3.
```bash
`pip install zappa`

`virtualenv env`
`source env/bin/activate`
`pip install zappa`
`pip install flask`
`pip install sumy`
`pip install numpy`
`python -c "import nltk; nltk.download('punkt')"`
	* copy the `nlkt_data` folder to your working directory
	* open `env/lib/python2.7/site-packages/nltk/data.py and modify line 92 or common path locations for the `nltk_data` directory to:
	```
	# Common locations on UNIX & OS X:
    path += [
        str('./nltk_data'),
        str('/tmp/nltk_data')
    ]
    ```
    This will allow for both cases when `slim_handler` in `zappa_settings.json` is `true` or `false`.
```

## Deployment

`zappa deploy dev`