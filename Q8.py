# Write a function that checks if the passed parameter is a valid URL or not.
#
# Please also explain your reasoning. Use only the concepts that we learned in class.
#
# Do not use any imports


def check_url(url):
    """
    Checks if the passed parameter is a valid URL or not.
    :param url:
    :return:
    """
    if url[0:8]== "https://" and " " not in url:
        print(f"{url} is valid")

    else:
        print(f"{url} is not valid")

check_url("https://wudgciuwgbciq.com")