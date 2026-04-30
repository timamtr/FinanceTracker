import datetime


def log_areket(func):

    def wrapper(*args, **kwargs):
        qazirgi_uaqyt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        natizhe = func(*args, **kwargs)

        print(f"[{qazirgi_uaqyt}] LOG: '{func.__name__}' funksiyasy satti oryndaldy.")

        return natizhe

    return wrapper