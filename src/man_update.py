import sqlite3
import arxivutils, arxivdb


def update(date):
	database, cursor = arxivdb.opendb()
	query = 'delete from arxiv where utcdate = '+date
    cursor.execute(query)

	# download the HTML of tonight's astro-ph listing
	listing = arxivutils.arxiv_update()

	# insert the articles into the DB and tag local authors automatically
	# the match_threshold is used to set the strictness of local author matching
	# smaller values are more relaxed, match_threshold ranges from 0.0 to 1.0.
	# the default value is 0.93
	arxivdb.insert_articles(listing)

	cursor.close()
    database.close()