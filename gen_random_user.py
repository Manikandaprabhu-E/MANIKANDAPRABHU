import json
import requests as rq

#https://jsonformatter.org/
#https://randomuser.me/api

def get_data(url):
    try:
        return rq.get(url).text
    except Exception as e:
        print("Unable to load URL")

def load_json(data):
    if not data is None:
        j = json.loads(data)
        fname = j["results"][0]["name"]["first"]
        lname = j["results"][0]["name"]["last"]
        fullname = j["results"][0]["name"]["title"]
        email = j["results"][0]["email"]
        age = j["results"][0]["dob"]["age"]
        gender = j["results"][0]["gender"]
        return fname, lname, fullname, email, age, gender


def main():
    url = "https://randomuser.me/api"
    values = load_json(get_data(url))

    if not values is None:
        print("First name: ", values[0])
        print("Last name: ", values[1])
        print("Fullname: ", values[2],values[0],values[1])
        print("email: ", values[3])
        print("age: ", values[4])
        print("gender: ", values[5])


if __name__ == '__main__':
    main()

