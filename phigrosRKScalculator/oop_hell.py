class Chart:
    def __init__(self,name=None,diffculty=None,constant=None,accuracy=None):
        
        if name == None:
            name = "NO NAME"
        if diffculty == None:
            diffculty = "SP"
        if constant == None:
            constant = "?"
        if accuracy == None:
            accuracy = 0

        self.name = name
        self.diffculty = diffculty
        self.constant = constant
        self.accuracy = accuracy

    def __str__(self) -> str:
        return f'Song Title: {self.name} \nChart Diffculty: {self.diffculty}\nChart Constant: {self.constant}\nAccuracy: {self.accuracy}'

song_list = []

def default_input_loop(input_message,error_message):
    while True:
        try:
            output = input(input_message)
            if output == "":
                raise ValueError
            break
        except ValueError:
            print(error_message)
            continue
    return output

title = default_input_loop('Enter the song title: ',"You can't leave it blank.")
diffculty = default_input_loop('Enter the chart diffculty: ',"You can't leave it blank.")
constant = default_input_loop('Enter the chart constant: ',"You can't leave it blank.")
accuracy = default_input_loop('Enter the accuracy: ',"You can't leave it blank.")

song_list.append(Chart(title,diffculty,constant,accuracy))

print(song_list)

for x in song_list:
    print(f'{x.name}')
