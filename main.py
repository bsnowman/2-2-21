import requests


def get_data(url: str):
    final_data = []
    response = requests.get(url)

    if response.status_code != 200:
        print(response.text)
        return []
    return final_data


def main():
    url = ""
    all_data = get_data(url)
    print(all_data)


if __name__ == '__main__':
    main()
