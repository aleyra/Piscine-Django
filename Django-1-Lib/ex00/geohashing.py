import sys
import antigravity


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Need 3 parameters : 2 floats for latitude and longitude and a date format 2005-05-26-10458.68")
        exit()
    try:
        antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), bytes(sys.argv[3], "UTF-8"))
    except Exception as err:
        print(err)
