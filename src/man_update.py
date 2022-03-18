import sys
import arxivutils, arxivdb


def update(date):
    success = False
    try:
        database, cursor = arxivdb.opendb()
        #query = 'delete from arxiv where utcdate = '+date
        cursor.execute('delete from arxiv where utcdate = (?)', (date,))
        database.commit()
        success = True
    except Exception as err:
        pass
    finally:
        cursor.close()
        database.close()

    if success:
        # download the HTML of tonight's astro-ph listing
        listing = arxivutils.arxiv_update()

        # insert the articles into the DB and tag local authors automatically
        # the match_threshold is used to set the strictness of local author matching
        # smaller values are more relaxed, match_threshold ranges from 0.0 to 1.0.
        # the default value is 0.93
        arxivdb.insert_articles(listing)
    else:
        print("Failed to update the database.")
        print(err)

if __name__=='__main__':
    date = sys.argv[1]
    update(date)
