def convert_minutes(minutes):
    days = minutes // 1440
    hours = (minutes % 1440) // 60
    return f"{days} kun {hours} soat"

def main():
    minutes = int(input("Vaqt oralig'i (daqiqalarda): "))
    print(convert_minutes(minutes))

main()
