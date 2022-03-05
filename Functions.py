import math

def seconds_minutes(seconds):
    if int(seconds)<60:
       return f'{seconds} seconds'
    else:
        minutes = int(seconds) / 60
        quotient = math.floor(minutes)
        remainder = (minutes - quotient) * 60
        return f'{quotient} minute(s), {int(remainder)} second(s)'


def hav(n):
    m = (1-math.cos(n))/2
    return m


def havinv(n):
    m = math.acos(1-2*n)
    return m


def havfor(lat_1, long_1, lat_2, long_2):
    lat_1 = math.radians(lat_1)
    lat_2 = math.radians(lat_2)
    long_1 = math.radians(long_1)
    long_2 = math.radians(long_2)
    m = hav(lat_2 - lat_1) + (1 - hav(lat_1 - lat_2) - hav(lat_1 + lat_2)) * hav(long_2 - long_1)
    return m


def angle_of_projection(range, muzzle_velocity):
    a = (math.asin(range*1000*9.81/(pow(muzzle_velocity, 2))))/2
    return a


def artillery_tof(angle, muzzle_velocity):
    t = 2*muzzle_velocity*math.sin(angle)/9.81
    t = round(t, 2)
    return t


def missile_tof(dist, mach):
    t = dist*1000/(343*mach)
    t = round(t, 2)
    return t


def missile_filter(directory, p):
    eligible_missile = []
    eligible_missile_1 = []

    for i in directory:
        if i.max_range > p > i.min_range:
            eligible_missile_1.append(i)
        else:
            pass
    eligible_missile_1.sort(key=lambda x: x.speed, reverse=True)
    for i in range(7):
        if i < len(eligible_missile_1):
            eligible_missile.append(eligible_missile_1[i])
            i += 1
        else:
            pass
    return eligible_missile


def artillery_filter(directory, p):
    eligible_artillery_1 = []
    eligible_artillery = []

    for i in directory:
        if i.max_range > p > i.min_range:
            eligible_artillery_1.append(i)
        else:
            pass
    eligible_artillery_1.sort(key=lambda x: x.muzzle_velocity, reverse=True)
    for i in range(3):
        if i < len(eligible_artillery_1):
            eligible_artillery.append(eligible_artillery_1[i])
            i += 1
        else:
            pass
    return eligible_artillery


def disp_ang(angle):
    a = round(math.degrees(angle), 3)
    return a

def missile_out(list_1, p):
    out = 'Distance is ' + str(round(float(p), 2)) + ' km \n \n'
    for i in list_1:
        out += '* ' + i.name + ' will destroy target in ' + seconds_minutes(missile_tof(p, i.speed)) + '\n'
    return out

def artillery_out(list_1, p):
    out = 'Distance is ' + str(round(float(p), 2)) + 'km \n \n'
    for i in list_1:
        out += '* ' + i.name + '\n will destroy target in ' \
               + seconds_minutes(artillery_tof(angle_of_projection(p, i.muzzle_velocity), i.muzzle_velocity)) \
               + '.\n Set angle of launching to ' + str(disp_ang(angle_of_projection(p, i.muzzle_velocity))) + '\n'
    return out
