import pickle
def append(file_name, record):
    f = open(file_name, "ab")
    pickle.dump(record, f)
    f.close()
record1 = {"name": 'Arun', "roll no.": 1, "marks": 95}
record2 = {"name": 'Dhruv', "roll no.": 2, "marks": 99}
append("ab.dat", record1)
append("ab.dat", record2)
def read(file_name):
    f = open(file_name, 'rb')
    while True:
        try:
            contents = pickle.load(f)
            print(contents)
        except EOFError:
            break
read('ab.dat')
print("-----")
def search(file_name, roll_no_record):
    f = open(file_name, 'rb')
    index = 0
    while True:
        try:
            contents = pickle.load(f)
            if contents['roll no.'] == roll_no_record:
                print("found", contents)
                f.close()
                return index
        except EOFError:
            break
        index += 1
    f.close()
    return -1
search_record_rollno = 1
search('ab.dat', search_record_rollno)
print("===")
def update(file_name, roll_no_record, new_marks):
    f = open(file_name, 'rb')
    record_list = []
    while True:
        try:
            rec = pickle.load(f)
            record_list.append(rec)
        except EOFError:
            break
    f.close()
    for record in record_list:
        if record['roll no.'] == roll_no_record:
            record['marks'] = new_marks
    f = open(file_name, "wb")
    for j in record_list:
        pickle.dump(j, f)
    f.close()


search2_record_rollno = 1
updated_marks = 90
update('ab.dat', search2_record_rollno, updated_marks)
print("***")
read("ab.dat")


def delete(file_name, roll_no_record):
    f = open(file_name, 'rb')
    record_list = []
    while True:
        try:
            rec = pickle.load(f)
            record_list.append(rec)
        except EOFError:
            break
    f.close()
    f = open(file_name, "wb")
    for record in record_list:
        if record['roll no.'] != roll_no_record:
            pickle.dump(record, f)
    f.close()


print("!!!!")
delete('ab.dat', 1)
print("@@@@")
read('ab.dat')
# removing all records
delete('ab.dat', 2)
