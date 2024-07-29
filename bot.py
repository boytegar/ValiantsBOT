import time
import requests
from datetime import datetime
import json
import random
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '0',
    "referer": "https://mini.playvaliants.com/",
}


def load_credentials():
    try:
        with open('token.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        # print("Token berhasil dimuat.")
        return queries
    except FileNotFoundError:
        print("File query_id.txt tidak ditemukan.")
        return 
    except Exception as e:
        print("Failed load  query:", str(e))
        return 

def load_boss():
    try:
        with open('list_boss.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        # print("Token berhasil dimuat.")
        return queries
    except FileNotFoundError:
        print("File list_boss.txt tidak ditemukan.")
        return 
    except Exception as e:
        print("Failed load list_boss:", str(e))
        return 

def getuseragent(index):
    try:
        with open('useragent.txt', 'r') as f:
            useragent = [line.strip() for line in f.readlines()]
        if index < len(useragent):
            return useragent[index]
        else:
            return "Index out of range"
    except FileNotFoundError:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
    except Exception as e:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'


def login(query):
    url = f'https://mini.playvaliants.com/api/login?{query}'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code >= 500:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 400:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def getdata(token):
    url = 'https://mini.playvaliants.com/api/user/data'
    headers['authorization'] = f'Bearer {token}'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code >= 500:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 400:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def get_mission(token):
    url = 'https://mini.playvaliants.com/api/user/missions'
    headers['authorization'] = f'Bearer {token}'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code >= 500:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 400:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def claim_daily_reward(token):
    url ='https://mini.playvaliants.com/api/rewards/claim'
    payload = {}
    headers['authorization'] = f'Bearer {token}'
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code >= 500:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 400:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def claim_mission(token, payload):
    url = 'https://mini.playvaliants.com/api/missions/claim'
    headers['authorization'] = f'Bearer {token}'
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code >= 500:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 400:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def taptap(token, payload):
    url = 'https://mini.playvaliants.com/api/gameplay/click'
    headers['authorization'] = f'Bearer {token}'
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code >= 500:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 400:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def put_squence(token, payload):
    url = 'https://mini.playvaliants.com/api/sequence'
    headers['authorization'] = f'Bearer {token}'
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code >= 500:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 400:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def upgrade_energy(token):
    url = 'https://mini.playvaliants.com/api/perks/energy-level-up'
    payload = {}
    headers['authorization'] = f'Bearer {token}'
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code >= 500:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 400:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def upgrade_multitap(token):
    url = 'https://mini.playvaliants.com/api/perks/click-level-up'
    payload = {}
    headers['authorization'] = f'Bearer {token}'
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code >= 500:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 400:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def refill(token):
    url = 'https://mini.playvaliants.com/api/user/refill-energy'
    payload = {}
    headers['authorization'] = f'Bearer {token}'
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code >= 500:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 400:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def unlocks(token, payload):
    url = 'https://mini.playvaliants.com/api/unlock'
    headers['authorization'] = f'Bearer {token}'
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code >= 500:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 400:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def combo_claim(token):
    url = 'https://mini.playvaliants.com/api/combo/claim'
    payload = {}
    headers['authorization'] = f'Bearer {token}'
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code >= 500:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 400:
            print(f"Status Code : {response.status_code} | {response.text}")
            return None
        elif response.status_code >= 200:
            return response.json()
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def get_data_by_id(list_boss, id):
    for boss in list_boss:
        if boss['id'] == id:
            return boss
    return None

def main():
    
    mission = input("Enter 'y' for mission or 'n' to skip: ")
    auto_battle = input("Enter 'y' for auto battle or 'n' to skip: ")
    auto_combo = input("Enter 'y' for auto combo or 'n' to skip: ")
    auto_update = input("Enter 'y' for auto update or 'n' to skip: ")
    if auto_update == 'y':
        max_level = int(input("Enter the maximum level upgrade: "))
    while True:
        list_combo = []
        queries = load_credentials()
        list_boss = load_boss()
        for index, token in enumerate(queries):
            useragent = getuseragent(index)
            headers['user-agent'] = useragent
            data_login = getdata(token)
            if data_login is not None:
                print(f'======== User {index+1} =========')
                energy = data_login.get('energy')
                energy_level = data_login.get('energy_level')
                click_level = data_login.get('click_level')
                refills = data_login.get('refills')
                print(f"Energy : {data_login.get('energy')}/{data_login.get('energy_cap')}")
                time.sleep(1)
                print("Claim daily reward")
                daily_reward = data_login.get('daily_reward')
                claimed = daily_reward.get('claimed')
                if claimed == True:
                    print('Daily reward claimed')
                else:
                    time.sleep(1)
                    data_daily = claim_daily_reward(token)
                    if data_daily is not None:
                        print(f"Daily claimed day {data_daily.get('day')} Reward : {data_daily.get('reward')}")
                        time.sleep(2)

                # payload = {'id': 36}
                # unlocks_boost = unlocks(token, payload)
                # if unlocks_boost is not None:
                #     print(f"{unlocks_boost.get('message')}")
                # time.sleep(2)

                if mission == 'y':
                    data_mission = get_mission(token)
                    if data_mission is not None:
                        list_mission = data_mission.get('missions')
                        for miss in list_mission:
                            if miss.get('type') == 'referral':
                                continue
                            claimed = miss.get('claimed')
                            id = miss.get('id')
                            if claimed == False:
                                time.sleep(2)
                                payload = {"id":id}
                                data_claim = claim_mission(token, payload)
                                if data_claim is not None:
                                    reward = data_claim.get('reward')
                                    print(f"Mission {id} claimed successfully | Reward : {reward}")

                if auto_combo == 'y':
                    combo = data_login.get('combo')
                    combo_completed = combo.get('combo_completed', False)
                    if combo_completed == True:
                        list_combo = combo.get('combo')
                        claimed = combo.get('claimed')
                        if claimed == False:
                            data_combo_claim = combo_claim(token)
                            if data_combo_claim is not None:
                                print(f"Status : {data_combo_claim.get('message')} Reward : {data_combo_claim.get('reward')}")
                    else:
                        for ids in list_combo:
                            time.sleep(2)
                            payload = {'id': ids}
                            data_unlocks = unlocks(token, payload)
                            if data_unlocks is not None:
                                print(f"Card Id : {ids} | Unlock perHours : {data_unlocks.get('unlock_experience_per_hour')} | Status Combo : {data_unlocks.get('combo_completed')}")
                        time.sleep(2)
                        data_combo_claim = combo_claim(token)
                        if data_combo_claim is not None:
                            print(f"Status : {data_combo_claim.get('message')} Reward : {data_combo_claim.get('reward')}")

                if auto_battle == 'y':
                    print('Start Auto Battle')
                    sequence = data_login.get('sequence')
                    complete = sequence.get('completed')
                    if complete == False:
                        enemy = sequence.get('enemy')
                        print(list_boss)
                        data_json = [json.loads(item) for item in list_boss]
                        data = get_data_by_id(data_json, enemy)
                        if data:
                            list = data['squence']
                            for index, i in enumerate(list):
                                time.sleep(2)
                                payload = {'sequence': i}
                                data_sequence = put_squence(token, payload)
                                if data_sequence is not None:
                                    message = data_sequence.get('message')
                                    if message == 'Sequence checked successfully':
                                        print(f"Attack {index+1} Done, Reward : {data_sequence.get('reward')}")

                        else:
                            print("Monster not found in Database")
                    else:
                        print('Battle Not Ready')
                        

                if auto_update =='y':
                    if energy_level < max_level:
                        print("Upgraded energy")
                        time.sleep(1)
                        data_upgrade = upgrade_energy(token)
                        if data_upgrade is not None:
                            print(f"Upgraded energy cap to {data_upgrade.get('energy_level')}")
                        time.sleep(2)
                    if click_level < max_level:
                        print("Upgraded multitap")
                        time.sleep(1)
                        data_upgrade = upgrade_multitap(token)
                        if data_upgrade is not None:
                            print(f"Upgraded energy cap to {data_upgrade.get('click_level')}")
                        time.sleep(2)

                

                while True:
                    time.sleep(2)
                    tap = random.randint(70,150)

                    if energy < tap:
                        tap = energy

                    payload = {"count":tap}
                    data_tap = taptap(token, payload)
                    if data_tap is not None:
                        user_energy = data_tap.get('user_energy')
                        reward = data_tap.get('reward')
                        print(f"Tapping {reward} Energy : {user_energy}")
                        energy = user_energy
                    
                    if energy < 50:
                        if refills < 6:
                            data_refill = refill(token)
                            if data_refill is not None:
                                time.sleep(1)
                                energy = data_refill.get('energy')
                                print(f'Refill energy {energy} | Remaining refills {refills-1}')
                                refills += 1
                            else:
                                print()
                                break
                        else:
                            print()
                            break
        # delay = random.randint(300, 500)
        # printdelay(delay)
        # time.sleep(delay)

def printdelay(delay):
    now = datetime.now().isoformat(" ").split(".")[0]
    hours, remainder = divmod(delay, 3600)
    minutes, sec = divmod(remainder, 60)
    print(f"{now} | Waiting Time: {hours} hours, {minutes} minutes, and {sec} seconds")


if __name__ == "__main__":
    main()