import sys
sys.path
#виводить перелік папок в яких Python здійснює пошук модулів. Даний перелік є списком і до нього можна
#додати папку використовуючи команду append (додає в кінець списку) або  insert (додає в визначену
# позицію за індексом).
sys.path.append('C:\\Users\\Ed\\PYTHON')
sys.path
#Ці зміни можна внести з Python, але вони є тимчасовими на час роботи сесії. Постійні зміни можна зробити
#змінивши змінну PATH в системі. В windows через - "Змінні оточення".