import pickle
class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])
def sanitize(time_string):
    # 如果'-'在time_string中，则splitter赋予'-'
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def get_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print("File Error: " + str(ioerr))
        return (None)

def put_to_store(files_list):
    all_athletes={}
    for each_file in files_list:
        ath = get_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open("athletes.pickle","wb") as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print("File Error(put_and_store):" +str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open("athletes.pickle","rb") as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print("File Error(get_from_store):" +str(ioerr))
    return(all_athletes)
the_files = ['resource/james2.txt','resource/julie2.txt','resource/mikey2.txt','resource/sarah2.txt']
data = put_to_store(the_files)
for each_athlete in data:
    print(data[each_athlete].name + '' + data[each_athlete].dob)


