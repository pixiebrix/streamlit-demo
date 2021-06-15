# PixieBrix Streamlit Demo

This repository contains an example [Streamlit](https://streamlit.io/) application that you can embed
on any page using [PixieBrix](https://www.pixiebrix.com/).


## Parsing Query Parameters in Streamlit

In your Streamlit app, parse the query parameters with `experimental_get_query_params`

```python
# https://github.com/streamlit/release-demos/blob/master/0.65/demos/query_params.py
query_params = st.experimental_get_query_params()
default = query_params["text"][0] if "text" in query_params else ""
```


## Passing Query Parameters

In PixieBrix, add a panel with an `@pixiebrix/iframe` brick. For the URL, specify
the URL for the Streamlit app with the query parameter:

```
https://share.streamlit.io/pixiebrix/streamlit-demo/main/demo.py?text={{ description | urlencode | safe }}
```

For text parameters, you can use the Nunjucks template engine to encode the parameter (in YAML, 
specify the `templateEngine: nunjucks` directive)