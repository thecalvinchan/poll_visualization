# Create your views here.

from django.shortcuts import render
from poll.models import PollResponse
from django.db.models import Count  

responses = PollResponse.objects.filter(completed__isnull=False)
total_responses = responses.count()
net_familiarity = responses.values('prop_30_familiarity').annotate(Count('pk')).order_by('-pk__count')

def inc_function(familiarity):
	income = responses.values('income_bracket').annotate(Count('pk')).order_by('-pk__count')
	data = {}
	for i in income:
   		count = responses.filter(income_bracket=i.get('income_bracket'),prop_30_familiarity__iexact=familiarity).aggregate(Count('pk'))['pk__count']
   		total_count = responses.filter(income_bracket=i.get('income_bracket')).aggregate(Count('pk'))['pk__count']
   		data[i.get('income_bracket')] = 100.0 * (float(count)/float(total_count)) 
   	return data 

def familiarity_function(income):
	familiarity = responses.values('prop_30_familiarity').annotate(Count('pk')).order_by('-pk__count')
	data = {}
	for i in familiarity:
   		count = responses.filter(prop_30_familiarity=i.get('prop_30_familiarity'),income_bracket__iexact=income).aggregate(Count('pk'))['pk__count']
   		total_count = responses.filter(income_bracket__iexact=income).aggregate(Count('pk'))['pk__count']
   		data[i.get('prop_30_familiarity')] = 100.0 * (float(count)/float(total_count)) 
   	return data 

def financial_function(income):
	familiarity = responses.values('prop_30_familiarity').annotate(Count('pk')).order_by('-pk__count')
	data = {}
	for i in familiarity:
   		count = responses.filter(prop_30_familiarity=i.get('prop_30_familiarity'),financial_aid__iexact=income).aggregate(Count('pk'))['pk__count']
   		total_count = responses.filter(financial_aid__iexact=income).aggregate(Count('pk'))['pk__count']
   		data[i.get('prop_30_familiarity')] = 100.0 * (float(count)/float(total_count)) 
   	return data    	     

def index(request):
	context = {
	        'responses': responses,
	        'total_responses': total_responses,
	        'net_familiarity': net_familiarity,
	        'fam5': inc_function(5),
	        'fam4': inc_function(4),
	        'fam3': inc_function(3),
	        'fam2': inc_function(2),
	        'fam1': inc_function(1),
	        'incgt120': familiarity_function("Annual income over $120,000"),
	        'inb80120': familiarity_function("Annual income between $80,000 - $120,000"),
	        'inclt80': familiarity_function("Annual income of $80,000 or less"),
	        'onlyfinaid': financial_function("I only have financial aid"),
	        'onlyloans': financial_function("I only have loans"),
	        'nofinaid': financial_function("I have neither financial aid nor loans"),
	        'bothfinaidloan': financial_function("I have both loans and financial aid")
	}
	return render(request, 'index.html', context)