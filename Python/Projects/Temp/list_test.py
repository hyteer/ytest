list = ['yt','see','tony']

if 'yt' in list:
	print 'yes'
else:
	print 'no'


dict = {'room1': {'num':2,'person':['yt','see','tony']}}

if 'see' in dict['room1']['person']:
	print 'yes'
else:
	print 'no'

dict['room1']['person'].append('silly')
print dict['room1']['person']

chatinfo = {}
chatinfo = dict
chatinfo['room2']={'num':0,'person':[]}
chatinfo['room2']['person'].append('Yongtang')

print chatinfo