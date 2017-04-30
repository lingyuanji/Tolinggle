# coding=utf-8
import sys
import requests
from workflow import Workflow

def main(wf):
    query = unicode(wf.args[0])
    query_string = u"http://linggle.com/query/"+(query.replace(" ","+"))
    try:
        answer = requests.get(query_string).json()
        if answer == []:
            wf.add_item(title = "No Results",\
             			subtitle = "modify your search",\
              			valid = False,\
               			icon = u"icon.png")
        else:
            for item in answer:
                phrase = " ".join(item["phrase"])
                sub = item["percent"]+" | "+item["count_str"]
                wf.add_item(title = phrase,\
                 			subtitle = sub,\
                  			arg = phrase,\
                  			valid = True,\
                   			icon = u"icon.png")
    except:
        wf.add_item(title = "Inquery Grammar Error",\
                    subtitle = "modify your search",\
                    valid = False,\
                    icon = u"icon.png")
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
