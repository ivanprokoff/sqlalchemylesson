from data import db_session
from data.users import User

db_session.global_init("db/colonisation.db")

dct = {'names': ['Ridley', 'John', 'John1', 'John2'],
       'surnames': ['Scott', 'Brown', 'Brown1', 'Brown2'],
       'ages': [21, 24, 27, 30],
       'positions': ['captain', 'crew member', 'crew member', 'crew member'],
       'specialities': ['research engineers', 'engineer', 'just funny guy', 'hmph'],
       'adresses': ['module_1', 'module 2', 'module 3', 'module 3'],
       'emails': ['scott_chief@mars.org', '1@mars.org', '2@mars.org', '3@mars.org']
}

for i in range(4):
    user = User()
    user.name = dct['names'][i]
    user.surname = dct['surnames'][i]
    user.age = dct['ages'][i]
    user.position = dct['positions'][i]
    user.speciality = dct['specialities'][i]
    user.address = dct['adresses'][i]
    user.email = dct['emails'][i]
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
