from Data.historic_data import getPeriodData

def execute():
    print("Started..")
    print(getPeriodData("SBIN.NS"))


if __name__ == "__main__":
    execute()