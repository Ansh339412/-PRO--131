import pandas as pd

data = pd.read_csv("Data.csv")
Star_names = data["Star_name"]
Brown_Dwarf_names = data["Brown_Dwarf_Name"]

Mass1 = []
for Mvalue in data['Mass_BrownDwarf']:
    Mvalue = float(Mvalue)
    Mvalue = Mvalue*1.989e+30
    Mass1.append(Mvalue)
data['Mass_BrownDwarf'] = Mass1

Mass2 = []
for Mvalue in data['Mass_Star']:
    Mvalue = float(Mvalue)
    Mvalue = Mvalue*1.989e+30
    Mass2.append(Mvalue)
data['Mass_Star'] = Mass2

Radius1 = []
for Rvalue in data['Radius_BrownDwarf']:
    Rvalue = float(Rvalue)
    Rvalue = Rvalue*6.957e+8
    Radius1.append(Rvalue)
data['Radius_BrownDwarf'] = Radius1

Radius2 = []
for Rvalue in data['Radius_Star']:
    Rvalue = float(Rvalue)
    Rvalue = Rvalue*6.957e+8
    Radius2.append(Rvalue)
data['Radius_Star'] = Radius2

star_gravity = []
for index, name in enumerate(Star_names):
    gravity = (float(Mass2[index])*5.972e+24) / (float(Radius2[index])
                                                 * float(Radius2[index])*6371000*6371000) * 6.674e-11
    star_gravity.append(str(gravity) + ' m/s2')

dwarf_gravity = []
for index, name in enumerate(Brown_Dwarf_names):
    gravity2 = (float(Mass1[index])*5.972e+24) / (float(Radius1[index])
                                                  * float(Radius1[index])*6371000*6371000) * 6.674e-11
    dwarf_gravity.append(str(gravity2) + ' m/s2')

data.insert(13, 'Gravity_Star', star_gravity)
data.insert(7, 'Gravity_Dwarf', dwarf_gravity)
df = pd.DataFrame(data)

df.to_csv('Data_With_Gravity.csv', index=False)
