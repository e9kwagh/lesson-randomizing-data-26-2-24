import random
from datetime import date, datetime, timedelta


def gen_date():
    year = 2024
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = datetime(year, month, day).strftime("%Y-%m-%d")
    return date


def create_assets(p):
    li = []
    now = datetime.now()

    for i in range(p):
        purchase_date = gen_date()
        if now > datetime.strptime(purchase_date, "%Y-%m-%d") :
            asset_dict = {"id": i , "purchase_date": purchase_date}
            li.append(asset_dict)
            break

    return li


def final(p):
    result = []
    for i in range(1, 9):
        assets = create_assets(i)
        result.extend(assets)
    return result


def rentals(p):
    rentals = []
    for i in range(1, p):
        dict = {}
        assets = final(p)
        start = gen_date()
        end = gen_date()
        ids = [row["id"] for row in assets]
        now = datetime.now().strftime("%Y-%m-%d")
        if start < end and start < now:
            dict = {
                "id": i,
                "asset_id": int(random.sample(ids, k=1)[0]),
                "start_date": start,
                "end_date": end,
            }
            rentals.append(dict)

    return rentals


if __name__ == "__main__":

    print(rentals(100))

# using Recursion


# def gen_date():


#         year = "2024"
#         month_d = random.randint(1, 12)
#         month = f'0{month_d}' if month_d <= 9 else str(month_d)
#         day_d = random.randint(1, 28)
#         day = f'0{day_d}' if day_d <= 9 else str(day_d)
#         date =  f'{year}-{month}-{day}'
#         return date


# def create_assets(p,li):


#     dict={}

#     now  =  datetime.now().strftime("%Y-%m-%d")
#     date =  gen_date()
#     if now > date :
#             dict = { "id": p , "purchase_date" :date}
#             li.append(dict)
#     else :
#             create_assets(p,li)

#     return li

# def final():
#     li =[]
#     for i in range(1,8):
#        final=  create_assets(i,li)
#        li.extend(final)
#     return li

# if __name__ == "__main__":
#     print(final())


# def result():
#        for i in range(1,9):
#             data = create_assets(i)


# if now < date :
#     if

# dict = { "id ": i }


# def generate_random_date():
#     start_date = date(2000, 1, 1)
#     end_date = date.today()

#     random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

#     return random_date

# print(generate_random_date())


# def gen_date():
#     year = "2024"
#     month_d =  random.randint(1, 12)
#     month = f'0{month_d}' if month_d <= 9 else str(month_d)
#     day_d = random.randint(1, 28)
#     day = f'0{day_d}' if day_d <= 9 else str(day_d)
#     return f'{year}-{month}-{day}'

# def create_assets(p):
#     assets = []
#     now = datetime.now().date()

#     for i in range(1, p+1):
#         days_ago = random.randint(1, 365)
#         purchase_date = now - timedelta(days=days_ago)

#         asset = {"id": i, "purchase_date": purchase_date.strftime("%Y-%m-%d")}
#         assets.append(asset)

#     return assets

# def result():
#     assets = create_assets(8)
#     for asset in assets:
#         print(asset)
