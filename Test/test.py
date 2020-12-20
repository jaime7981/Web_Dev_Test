import json
import requests
from requests.exceptions import HTTPError

url_list = ["https://www.hunterdouglas.cl/"]

for url in url_list:
    try:
        response = requests.post(url)
        response.raise_for_status()

    except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')

    except Exception as err:
        print(f'Other error occurred: {err}')

    else:
        print(response.text + "\n")
        check = str(input("Desea copiar la pagina? (S)"))
        if check == "s" or check == "S":
            check = str(input("Nombre del archivo"))
            if len(check) == 0:
                open(("html_copy.html"), "w").write(str(response.text))
            else:
                open((check + ".html"), "w").write(str(response.text))


