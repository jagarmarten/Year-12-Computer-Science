pages = ["home", "contact", "login"]
outboundLinks = [["contact", "login"], ["home"], ["contact"]]
inboundLinks = [1,2,1]

dampingFactor = 0.85

initialPageRank = [1,1,1]
pageRank = [0,0,0]

for x in range(3):
    sum = 0
    currentPage = pages[x] #Get the current page
    outboundLinksFromPage = outboundLinks[x] #Get otubound links from the current page
    for y in range(len(outboundLinksFromPage)):
        pageRank[x] = 0.15 + 0.85*(initialPageRank[x]/inboundLinks[pages.index(outboundLinksFromPage[y])])
        # To calculate the pageRank I want to get the index of the page where a link to page[x] was found
        # Then I 
        
        print(pageRank)
    #END FOR
#END FOR