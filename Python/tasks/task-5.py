"""
Write a function that when given a URL as a string, parses out just the domain
name and returns it as a string.
"""
from urllib.parse import urlparse


def domain_name(url):
    parse_url = urlparse(url)
    if parse_url.netloc == '' and parse_url.path != '':
        if parse_url.path.startswith('www.'):
            parse_url = parse_url.path[4:]
        else:
            parse_url = parse_url.path.split('/')[0]

    elif parse_url.netloc != '':
        if parse_url.netloc.startswith('www.'):
            parse_url = parse_url.netloc[4:]
        else:
            parse_url = parse_url.netloc

    result = parse_url.split('.')[0]

    # print(result)
    return result


# domain_name("http://google.com")
# domain_name("http://google.co.jp")
# domain_name("www.xakep.ru")
# domain_name("https://youtube.com")

# domain_name("http://github.com/carbonfive/raygun")
# domain_name("http://www.zombie-bites.com")
# domain_name("https://www.cnet.com")
# domain_name("jjik86nfjvxi3zz5idojobvfx1k7m.com/fd/sdfe432")

