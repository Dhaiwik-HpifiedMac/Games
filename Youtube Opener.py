import webbrowser
url_fragment = input("Which Youtube channel do you wan to go to?  ")
link = "https://youtube.com/@" + url_fragment
webbrowser.open_new(link)
