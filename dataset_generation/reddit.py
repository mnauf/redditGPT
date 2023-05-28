import requests


def get_100_posts_from_this_community(community, after_keyword, output):
    if after_keyword is None:
        return output, after_keyword

    post_result, after_keyword = get_posts(community, after_keyword)

    for index, children in enumerate(post_result):
        output += post_result[index]["data"]["title"]
        output += "\n\n"
        output += post_result[index]["data"]["selftext"]
        output += "\n\n"

        post_url = "https://oauth.reddit.com/" + post_result[index]["data"]["permalink"]
        output += get_comments(post_url)

    return output, after_keyword


def get_posts(community, after_keyword):
    # Reddit API only fetches maximum 100 posts at a time. "after" parameter helps to get the next new 100 posts.
    res = requests.get(f"https://oauth.reddit.com/r/{community}/search/?q=imran%20khan&restrict_sr=1&sort=relevance&t=year",
                       headers=headers, params={"limit": 100, "after": after_keyword})
    post_result = res.json()["data"]["children"]
    after_keyword = res.json()["data"]["after"]
    return post_result, after_keyword


def get_comments(post_url):
    text = ""
    res = requests.get(post_url,
                       headers=headers)

    comment_result = res.json()[1]["data"]["children"]

    for index, children in enumerate(comment_result[:-1]):
        author = comment_result[index]["data"]["author"]
        comment = comment_result[index]["data"]["body"]
        if author == "AutoModerator" or author == "autotldr":
            continue

        if comment != "[removed]" and comment != "[deleted]":
            text += comment
            text += "\n\n"

    return text


def write_to_file(text):
    with open("dataset_1.txt", "w", encoding="utf-8") as fp:
            fp.write(text)


def get_header():
    # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
    auth = requests.auth.HTTPBasicAuth('CLIENT_ID', 'SECRET_TOKEN')

    # here we pass our login method (password), username, and password
    data = {'grant_type': 'password',
            'username': '',
            'password': ''}

    # setup our header info, which gives reddit a brief description of our app
    headers = {'User-Agent': 'MyBot/0.0.1'}

    # send our request for an OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    # convert response to JSON and pull access_token value
    TOKEN = res.json()['access_token']

    # add authorization to our headers dictionary
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    return headers


if __name__ == '__main__':
    headers = get_header()
    output = ""
    communities = ["AskMiddleEast", "worldnews", "Pakistan"]
    for community in communities:
        after_keyword = ""
        for page in range(10):
            output, after_keyword = get_100_posts_from_this_community(community, after_keyword, output)

    write_to_file(output)