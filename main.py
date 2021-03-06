from data import db_session
from data.users import User
from data.jobs import Jobs


def create_job(team_leader_, job_, work_size_, collaborators_, start_date_, is_finished_):
    job = Jobs()
    job.team_leader = team_leader_
    job.job = job_
    job.work_size = work_size_
    job.collaborators = collaborators_
    job.start_date = start_date_
    job.is_finished = is_finished_
    db_sess_ = db_session.create_session()
    db_sess_.add(job)
    db_sess_.commit()



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
create_job(1, 'deployment of residential modules 1 and 2', 15, '2, 3', 'now', False)
