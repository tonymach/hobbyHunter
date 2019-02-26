from collections import Counter
import re
from random import randint
from search.models import Page, Index, Keyword, merchantPages

class pageFuncs(object):
    """
    Contains all page funcs such as creating and editing
    """
    class creation:
        """
        (string, string, string, int, decimal, decimal, decimal) => Bool
        Will create a page with supplied things
        """
        def post(merchant, title, description, averageCost, image, lat=1.11,lon=1.11, stars=5):
            keywords = Parse.q(title)
            pageId = randint(10**10,10**11)
            pageId = str(pageId)
            averageCost = int(averageCost)
            if description == 'banana':
                description = 'This course is not for the light of heart, you will experience the pinacle of over ten seconds of random thinking. All of which put together will allow you to be absolutely mesmerized by the complete and utter idiocy. Banana'
            try:
                # Creates and saves a page
                page = Page.objects.create(pageId=pageId,description=description, title=title, stars=stars,lat=lat,lon=lon,averageCost=averageCost,country='CA', merchant=merchant)
                page.save()
                page.mainImage  = image
                page.save()
                # Create a link between merchant and Pages

                # If there is a link, ignore otherwise create
                if not merchantPages.objects.filter(pk=merchant):
                    link = merchantPages.objects.create(merchant = merchant)
                else:
                    link = merchantPages.objects.get(pk=merchant)
                if link.endPoints == None:
                    link.endPoints = []

                link.endPoints.append(pageId)
                link.save()

                for i in keywords:
                    if not Keyword.objects.filter(pk=i):
                        keyword = Keyword.objects.create(keyword=i)
                    else:
                        keyword = Keyword.objects.get(pk=i)
                    if keyword.pages == None:
                        keyword.pages = []
                    print('none such')
                    keyword.pages.append(pageId)
                    keyword.save()
                return True
            except:
                return False

        def postImage(page, image):
            try:
                temp = Page.objects.get(pk=page)
                temp.mainImage  = image
                temp.save()
                return True
            except:
                return False

    class manage:
        """
        Handles things like editing fields and all
        """
        def edit(id,field, data):
            """
            (string,string, data) => Bool
            """
            try:
                page = Page.objects.get(pk=id)
                page[field] = data
                page.save()
                return True
            except:
                return False

        def delete(id):
            """
            (string) => Bool
            """
            try:
                Page.objects.get(pk=id).delete()
                return True
            except:
                return False

class Query(object):
    """
    Sends a Query and goes through the madness
    """
    def proccess(query):
        original = query
        results = []
        # Shortens the query
        short = Parse.shorten(query)
        # Parses and sets array of the query
        parsed = Parse.q(short)
        # Checks if query has a direct object link
        if Index.objects.filter(pk=query).exists():
            results+= index.endPoints
            print(results)
        else:
            # Return array of keyword links
            results+= Query.keywords(parsed)

        results = Parse.organizeByFrequency(results)

        return results

    def keywords(queries):
        r = []
        for i in queries:
            if Keyword.objects.filter(pk=i).exists():
                x = Keyword.objects.get(pk=i)
                print(x.pages)
                r+=x.pages
        return r

class Parse(object):
    """
    Parse Queries and all usage: Parse.q('Banana dance')
    """

    # Shortens by removing common endings and removes crazy characters
    def shorten(x):
        x.replace('ing', '').replace('ed','').replace('-','')
        # x = re.sub('[^A-Za-z0-9]+', '', x)
        x = x.lower()
        return x

    # Shotens and splits to rturn array
    def q(x):
        x = Parse.shorten(x)
        y = x.split()
        return y

    # Found on overflow https://stackoverflow.com/questions/16006630/how-to-organize-list-by-frequency-of-occurrence-and-alphabetically-in-case-of-a
    # works really well
    def organizeByFrequency(x):
        counts = Counter(x)
        words = sorted(counts, key=lambda word: (-counts[word], word))
        return words

        #
        # response_data['result'] = 'Create post successful!'
        # response_data['postpk'] = post.pk
        # response_data['text'] = post.text
        # response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        # response_data['author'] = post.author.username
        #
        # return HttpResponse(
        #     json.dumps(response_data),
        #     content_type="application/json"
        # )
