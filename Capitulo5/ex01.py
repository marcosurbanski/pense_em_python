import time

def time_calc():
    
    time_start = time.gmtime(0)
    time_epoch = (time.asctime(time_start))
    current_date = time.strftime("%a, %d, %b, %Y %H:%M:%S", time.localtime())
    sum_epoch = time.mktime(time.localtime())
    

    days_since_epoch = sum_epoch / (60 * 60 * 24)

    print_date(current_date, time_epoch, sum_epoch)
    print(f"Days since epoch: {int(days_since_epoch)}")

def print_date(date, time_epoch, sum_epoch):
    print(f"{date} \n{time_epoch} \n {sum_epoch}")


if __name__ == "__main__":
    time_calc()