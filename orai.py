def maganhangzo_torles(s):
    maganhangzok = "aáeéiíoóö˝ouúü˝uAÁEÉIÍOÓÖ˝OUÚÜ˝U"
    massalhangzos_s = ""
    for k in s:
        if k not in maganhangzok:
            massalhangzos_s += k
    return massalhangzos_s

print(maganhangzo_torles("informatika"))
print(maganhangzo_torles("aábeéiífoóö˝oujúü˝upAÁEÉIÍOÓÖ˝OUÚÜ˝Us"))