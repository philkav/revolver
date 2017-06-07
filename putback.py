import redis

db_host = 'localhost'
db_port = 6379
r = redis.StrictRedis(host=db_host, port=db_port, db=0)

class putback:
	def __init__(self, build, rev):
		self.rev = rev
		self.build = build

	def exists(self):
		return False	

	def write(self):
		r.rpush('{}:{}'.format('putbacks',self.build),self.rev)
		return True

