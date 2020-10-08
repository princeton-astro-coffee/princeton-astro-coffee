# -*- coding: utf-8 -*-

'''This is the configuration file template for astro-coffee.

'''

import os.path

####################
## BASIC SETTINGS ##
####################

# The server will place its files in the base directory. All other paths are
# relative to this directory.
basedir = '{{ basedir }}'

# This is where the server keeps the page templates. Edit these to change the
# various UI elements of the webpages.
template_path = os.path.join(basedir, 'templates')

# This is where the server keeps its JS and CSS files. Edit the CSS files in
# {asset_path}/css/astrocoffee.css as necessary
asset_path = os.path.join(basedir, 'static')

# This defines the number of background workers used by the server.
max_workers = 2

# This defines the TCP port on which the server listens.
server_port = 5005

# This defines the address on which the server listens. '0.0.0.0' means it
# listens on all interfaces (so you can access it from other computers by
# http://ip-address-of-server:server_port/astro-coffee). '127.0.0.1' means it
# only listens for connections from localhost so you can only browse to
# http://127.0.0.1:server_port/astro-coffee on the computer where the server
# runs.
server_address = '0.0.0.0'

# The server will serve all of its pages starting from this URL as the root,
# e.g. the current arXiv listings page will be served at:
# {base_url}/papers/today.
# Set this to '' to serve all pages from the root URL: /.
base_url = '/astro-coffee'


###################
## LOCAL AUTHORS ##
###################

# this is the path to the local authors CSV that will be used to initially
# populate the list of local authors. this should contain rows in the following
# format:
#
# author_name,author_email,author_special_affiliation
#
# author_special_affiliation can be an empty string to indicate the author is
# associated with the main group of people that'll be using the server. If the
# author belongs to another institution but should be counted as a local author,
# include that institution's name in this column.
local_author_csv = os.path.join(basedir, 'local-authors.csv')


####################
## AUTHENTICATION ##
####################

# This is the SQLAlchemy database URL for the database tracking users, logins,
# signups, etc.
authdb_url = 'sqlite:///%s' % os.path.join(basedir,'.authdb.sqlite')

# This is the secret token used to sign session cookies
session_secret = '{{ session_secret }}'

# These are session settings.
session_settings = {
    'expiry_days': 30,
    'cookie_name':'astrocoffee_session',
    'cookie_secure':True
}

# These are API settings.
api_settings = {
    'ratelimit_active':True,
    'version':1,
    'expiry_days':30,
    'issuer':None
}

# This is the cache directory for the server.
cache_dir = '/tmp/astrocoffee-server'


###############
## DATABASES ##
###############

# This is the SQLAlchemy database URL for the main astro-coffee database.
database_url = 'sqlite:///%s' % os.path.join(basedir,'astro-coffee.sqlite')


############
## PEOPLE ##
############

# These are the contact details of the person responsible for this server.
admin_name = 'Admin Contact'
admin_email = 'coffeeadmin@institution.edu'

# These are emails of people that will be automatically promoted to the staff
# privilege level when they sign up for an account. These accounts can tag/untag
# local author papers and manually run an arxiv update.
staff_email_addresses = {
    'staff1@example.edu',
    'staff2@example.edu',
}

# These are domain names of the email address allowed to sign up for an
# account. Signed up users can vote, reserve, and sign-up to be presenters from
# anywhere (and not just from the locations defined below in ACCESS CONTROL)
email_domains = {
    'astro.example.edu',
    'institute.edu',
}


############
## PLACES ##
############

# The name of room where Astro Coffee happens.
room = 'Example Room'

# The name of building where Astro Coffee happens.
building = 'Example Hall'

# The name of department where Astro Coffee happens.
department = 'Department of Astronomy'

# The name of institution where Astro Coffee happens.
institution_full_name = 'Example University'
institution_short_name = 'Example'

# The URL of the department where Astro Coffee happens
department_url = 'https://www.astro.example.edu'

# The URL of the institution where Astro Coffee happens
institution_url = 'https://www.example.edu'

# path to the logo for the department relative to the assets_dir sub directory
# defined above. Copy your logo into this directory before using it here.
institution_logo_file = 'images/logo.png'


###########
## TIMES ##
###########

# The default voting start time is 21:00 local time.
voting_start_localtime = '21:00'

# The default voting cutoff time is 10:29 local time.
voting_end_localtime = '10:29'

# Astro Coffee at Princeton is Monday through Friday in local time
# arXiv is updated Monday through Friday between 00:00 to 01:00 UTC
# This will set when the server will update its listings
coffee_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Astro Coffee at Princeton is at 10:30 local time.
coffee_at_localtime = '10:30'

# This sets the maximum days allowed to keep a paper in the reserved list.
reserve_days = 5

# These set the update times in UTC for each day of coffee_days.
# We update late on Monday UTC because the arXiv updates later that day.
update_utc_times = ["00:50", "00:40", "00:40", "00:40", "00:40"]
update_utc_days = coffee_days


####################
## ACCESS CONTROL ##
####################

# This is the path to the MaxMind GeoIP2 city database used for IP address
# location and geofencing of voting attempts. Download updates from:
# http://dev.maxmind.com/geoip/geoip2/geolite2/.
geoip_database = os.path.join(basedir, 'GeoLite2-City.mmdb')

# These are ISO codes for countries and subdivisions from where voting is
# allowed (http://en.wikipedia.org/wiki/ISO_3166-2).

# Set allowed_regions to None if you want only the IP addresses in the ranges
# described below in voting_cidr to be able to vote on papers.
allowed_regions = {
    'US': ['NJ','NY','PA'],
}

# These are IP address range definitions in CIDR format (comma-separated)
# https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation.
# Look these up for your institution using https://ipinfo.io/ (find the AS
# number and click on it to get the IP address ranges associated with it).

# These are local (intranet) associated network ranges that allow all actions.
internal_cidr = {
    '10.0.0.0/8',
    '172.16.0.0/12',
    '192.168.0.0/16',
    '127.0.0.0/8',
}

# These are IP address ranges for users that will have voting permissions. These
# will be applied before any geo-fencing.
voting_cidr = {
    '128.0.0.0/8',
} | internal_cidr

# These are IP address range definitions for users that will have reserving
# permissions. These should be ideally restricted to the department only.
reserve_cidr = {
    '128.0.0.0/8',
} | internal_cidr

# These are IP address range definitions for users that will sign up to present
# papers. These should be ideally restricted to the department only.
present_cidr = {
    '128.0.0.0/8',
} | internal_cidr

# These are IP address range definitions for users that will have edit
# permissions. These should be ideally restricted to the department only.
edit_cidr = {
    '128.0.0.0/8',
} | internal_cidr


###########################
## EMAIL SERVER SETTINGS ##
###########################

# the address of the email server that will send out account verification and
# reminder emails
email_server = 'smtp.gmail.com'

# the SMTP port number to use
email_port = 587

# the username of the email server account to use
email_username = 'username@gmail.com'

# the password of the email server account
email_password = 'google-app-password-for-gmail-goes-here-if-you-use-gmail-here'

# the name and email address the emails will be addressed from
email_sender_name = admin_name
email_sender_address = admin_email