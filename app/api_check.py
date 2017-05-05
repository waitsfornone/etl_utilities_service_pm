def validate_api(api_key):
    api_chunks = api_key.split('-')
    if len(api_chunks) == 9 and all(len(chunk) == 5 for chunk in api_chunks):
        return True
    else:
        return False
