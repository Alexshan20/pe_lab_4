import operator
import pickle

filename = 'students.csv'
newFilename = 'students_changed.csv'
pickleFilename = 'pickleName'


class File:
    def write_csv(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
            return [x.split(';') for x in data.split('\n')]
    def sort(self, data, i):
        return sorted(data, key=operator.itemgetter(i))
    def age(self, data):
        return [x for x in data[1:] if int(x[2]) > 22]
    def record(self, data, newFilename, limiter=';'):
        data.append(['11', 'Шаньгина Алена Анатольевна', '22', '351066'])
        data = '\n'.join([limiter.join(x) for x in data])
        with open(newFilename, "w", encoding="utf-8") as f:
            f.write(data)
    def w_pickle(self, data, pickleFilename):
        with open(pickleFilename, "wb") as f:
            pickle.dump(data, f)
    def r_pickle(self, pickleFilename):
        with open(pickleFilename, "rb") as f:
            return pickle.load(f)





q1 = File().write_csv(filename)
q2 = File().sort(q1, 1)
q3 = File().age(q1)
q4 = File().record(q1, newFilename)
q5 = File().write_csv(newFilename)
q6 = File().w_pickle(q1, pickleFilename)
q7 = File().r_pickle(pickleFilename)
print(f'Задание 2: {q1}')
print(f'Задание 2.1: {q2}')
print(f'Задание 2.2: {q3}')
print(f'Задание 2.4: {q5}')
print(f'Задание 2.5: w_pickle')
print(f'Задание 2.6: {q7}')
