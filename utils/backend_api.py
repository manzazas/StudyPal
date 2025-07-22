import requests


def get_flaschards(notes,num):
    response = requests.post("https://localhost:5000/flaschards",json = {
        "notes": notes,
        "num_of_cards": num
    })

    return response.json()