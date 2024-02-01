
def eventlist(l,k):
	if k>len(l):
		return "Invalid no."
	event= [l[0]]
	for i in range(1,len(l)):
		#start date of current event
		start_date = l[i][0]
		#start date comparison
		last_event_duration = [u for u in range(event[-1][0],event[-1][1]+1)]
		
		if start_date in last_event_duration:
			continue
		else:
			if len(event)<k:
				event.append(l[i])
	return event


a = [[1,2,4],[2,3,1],[3,4,3]]
k = 2

print(eventlist(a,k))
