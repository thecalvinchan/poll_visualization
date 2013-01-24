from django.db import models

class PollResponse(models.Model):
    """
    A response to the Daily Bruin poll.
    """
    # Basics & setup
    response_id = models.PositiveIntegerField()
    completed = models.DateTimeField(null=True, blank=True)
    last_page_seen = models.IntegerField()
    start_langualge = models.CharField(max_length=50)
    last_action = models.DateTimeField(null=True)
    started = models.DateTimeField(null=True)
    ip_address = models.IPAddressField(blank=True, null=True)
    referrer_url = models.CharField(max_length=500, blank=True, null=True)
    
    # Demographics
    what_year = models.CharField(max_length=500, blank=True, null=True)
    major = models.CharField(max_length=500, blank=True, null=True)
    second_major = models.CharField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    african_american = models.BooleanField()
    american_indian = models.BooleanField()
    asian = models.BooleanField()
    hispanic = models.BooleanField()
    white = models.BooleanField()
    domestic_race_unknown = models.BooleanField()
    international_race_unknown = models.BooleanField()
    
    # Questions
    income_bracket = models.CharField(max_length=500, blank=True, null=True)
    financial_aid = models.CharField(max_length=500, blank=True, null=True)
    residency_status = models.CharField(max_length=500, blank=True, null=True)
    voter_status = models.CharField(max_length=500, blank=True, null=True)
    vote_2008 = models.CharField(max_length=500, blank=True, null=True)
    support_2008 = models.CharField(max_length=500, blank=True, null=True)
    worked_on_campaign = models.BooleanField()
    participated_student_protests = models.BooleanField()
    political_student_group = models.BooleanField()
    political_party = models.CharField(max_length=500, blank=True, null=True)
    president_2012 = models.CharField(max_length=500, blank=True, null=True)

    # Below is a list of issues that have been discussed in the 2012 elections.
    # On a 1-10 scale, please rate how important the candidates' stances on these issues are,
    # in terms of influencing who you will vote for. 
    #
    # Answered on a scale of 1-5
    # 1 = not important
    # 5 = highly important
    economy = models.IntegerField(null=True)
    job_market = models.IntegerField(null=True)
    international_affairs = models.IntegerField(null=True)
    immigration = models.IntegerField(null=True)
    education = models.IntegerField(null=True)
    healthcare = models.IntegerField(null=True)
    social_issues = models.IntegerField(null=True)

    # positive/negative type questions
    overall_obama_politics = models.CharField(max_length=500, blank=True, null=True)
    obama_education_policies = models.CharField(max_length=500, blank=True, null=True)
    obama_immigration_policies = models.CharField(max_length=500, blank=True, null=True)

    # Another 1-5 question
    prop_30_familiarity = models.IntegerField(null=True)
    prop_30_vote = models.CharField(max_length=500, blank=True, null=True)
    prop_30_affect_uc = models.CharField(max_length=500, blank=True, null=True)

    # Times
    total_time = models.FloatField(null=True)
    general_information_time = models.FloatField(null=True)
    presidential_election_time = models.FloatField(null=True)
    tax_measure_time = models.FloatField(null=True, blank=True)