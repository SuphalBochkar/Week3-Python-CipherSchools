# def make_dic(n):
#     d = {}
#     for i in range(n):
#         i,j = input().split(',')
#         d[i] = j
#     return d

# for i in make_dic(int(input())).items():
#     print(i)


user = {}
name = input( 'What is your name: ')
age = input( 'what is your age: ')
fav_movie = input('your fav movies Deparated by comma: ').split(',')
fav_songs = input('your fav songk separated by comma: ').split(',')
user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movie
user['fav_songs'] = fav_songs

for key , value in user.items() :
    print(f'{key} : {value}')
