class Album:
    def __init__(self, title, group, track_list):
        self.title = title
        self.group = group
        self.track_list = track_list
    def get_tracks(self):
        print(f'Список треков в альбоме "{self.title}":')
        print()
        for track in self.track_list:
            track.show()
    def add_track(self, new_track):
        self.track_list.append(new_track)
        print(f'В альбом "{self.title}" добавлен трек "{new_track.title}"')
    def get_duration(self):
        sum_time = 0
        for track in self.track_list:
            sum_time += track.time
        print(f'Длительность альбома "{self.title}" составляет {sum_time} секунд')        

class Track:
    def __init__(self, title, time):
        self.title = title
        if isinstance(time, int): 
            self.time = time
        else:
            print(f'Вы указали не верное время трека "{self.title}". Нужно укзать число')
            return
    def show(self):
        print(f'"{self.title}" - {self.time}')

track_one = Track('Тихие', 123)
track_two = Track('Белые', 444)
track_three = Track('Юркие', 222)

track_four = Track('Моя последняя песня', 1000)
track_five = Track('Моя самая последняя песня', 1)
track_six = Track('Моя непоследняя песня', 22)

bonus_track = Track('Все зависит от нас, сомих', 666)


albom_one = Album('Крутой альбом', 'Группа "Мыши"', [track_one, track_two, track_three])
albom_two = Album('Профессионал', 'Группа "Я не вру"', [track_four, track_five, track_six])

albom_one.get_duration()
# print()
# albom_one.get_tracks()
# print()
# albom_one.add_track(bonus_track)
# print()
# albom_one.get_tracks()
# print()
albom_two.get_duration()
# print()
# albom_two.get_tracks()
# print()
# albom_two.add_track(bonus_track)
# print()
# albom_two.get_tracks()
# print()
# mistake_track = Track('Еще один трек', 'одинадцать')