# PageSpeed for Wordpress
#
# web: https://onlinemarketingscience.com
# twitter: @MarvinJoers
# author: Marvin Jörs
# date: 2017-11-26
#
#    

import argparse
import sys
import urllib.request, json 

# Eingabe: 
# Beispiel: python pagespeed.py http://example.com
# .....
# - Reduce server response time (50.42952664502194%)
# => Installation des Plugins: wordpress.org/plugins/p3-profiler/.
# => Plugins deinstallieren, die nicht wirklich gebraucht werden.
# - Eliminate render-blocking JavaScript and CSS in above-the-fold content (35.92486314872445%)
# => Installation des Plugins: wordpress.org/plugins/autoptimize/.
# => Installation des Plugins: wordpress.org/plugins/w3-total-cache/.
# => Anleitung folgen: http://www.wpbeginner.com/wp-tutorials/how-to-fix-render-blocking-javascript-and-css-in-wordpress/

argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('path', type=str,
                       help=('URL für den PageSpeed-Test'))
args = argparser.parse_args()


# Bitte hier den API-Key aus der Developer Console eintragen
###################################################
api_key = 'INSERT_API_KEY'
###################################################

# Wir wollen nur die Aspekte, die einen ruleImpact von größer 0 haben!
filtered_array = []

def a_filter(an_array):

    if(an_array['ruleImpact'] != 0):
     filtered_array.append(an_array)
   

def sticking():
    basic_url = "https://www.googleapis.com/pagespeedonline/v1/runPagespeed?url="
    parameter = "&key="
    url_input = basic_url + args.path + parameter + api_key
  
    return url_input

with urllib.request.urlopen(sticking()) as url:
    data = json.loads(url.read().decode())
    
# Generelle Informationen für den Nutzer
print("###############################")
print("URL der Seite: " + data['id'])
print("Titel der Seite: " + data['title'])
print("Score: " +  str(data['score']))
print("###############################")

# Untersuchte Aspekte
redirects = data['formattedResults']['ruleResults']['AvoidLandingPageRedirects']
compression = data['formattedResults']['ruleResults']['EnableGzipCompression']
caching = data['formattedResults']['ruleResults']['LeverageBrowserCaching']
responseTime = data['formattedResults']['ruleResults']['MainResourceServerResponseTime']
minify_css = data['formattedResults']['ruleResults']['MinifyCss']
minify_html = data['formattedResults']['ruleResults']['MinifyHTML']
render_blocking = data['formattedResults']['ruleResults']['MinimizeRenderBlockingResources']
visible_content = data['formattedResults']['ruleResults']['PrioritizeVisibleContent']
optimize_images = data['formattedResults']['ruleResults']['OptimizeImages']


a_filter(redirects)
a_filter(compression)
a_filter(caching)
a_filter(responseTime)
a_filter(minify_css)
a_filter(minify_html)
a_filter(render_blocking)
a_filter(visible_content)
a_filter(optimize_images)

print("Dringlichkeit ist hier in Prozent angegeben: ")

sum_of_impact = 0

for element in filtered_array:
    sum_of_impact += element['ruleImpact']

for element in filtered_array:

 if (element['localizedRuleName'] == "Optimize images"):
        print("- " + element['localizedRuleName'] + " (" + str((element['ruleImpact']/sum_of_impact)*100) + "%)")
        print("Für dieses Problem eignen sich folgende Vorgehensweisen")
        print("=> Installation des Plugins: wordpress.org/plugins/optimus/.")
        print("=> Bilder einzeln über compress.io komprimieren.")
        print("=> Bildgrößen anpassen: Nur Bilder in der Größe hochladen, in denen sie gebraucht werden.")
        print("###############################")

 if (element['localizedRuleName'] == "Avoid landing page redirects"):
        print("- " + element['localizedRuleName'] + " (" + str((element['ruleImpact']/sum_of_impact)*100) + "%)")
        print("Überprüfe, ob zu viele Redirects eingerichtet sind.")
        print("###############################")

 if (element['localizedRuleName'] == "Enable compression"):
        print("- " + element['localizedRuleName'] + " (" + str((element['ruleImpact']/sum_of_impact)*100) + "%)")
        print("Anleitung folgen: https://torquemag.io/2016/04/enable-gzip-compression-wordpress/.")
        print("###############################") 

 if (element['localizedRuleName'] == "Minify CSS"):
        print("- " + element['localizedRuleName'] + " (" + str((element['ruleImpact']/sum_of_impact)*100) + "%)")
        print("=> Installation des Plugins: wordpress.org/plugins/autoptimize/.")
        print("###############################") 

 if (element['localizedRuleName'] == "Minify HTML"):
        print("- " + element['localizedRuleName'] + " (" + str((element['ruleImpact']/sum_of_impact)*100) + "%)")
        print("=> Installation des Plugins: wordpress.org/plugins/autoptimize/.")
        print("###############################")  

 if (element['localizedRuleName'] == "Leverage browser caching"):
        print("- " + element['localizedRuleName'] + " (" + str((element['ruleImpact']/sum_of_impact)*100) + "%)")
        print("=> Anleitung folgen: https://www.sir-apfelot.de/wordpress-ladezeit-in-20-sekunden-optimieren-leverage-browser-caching-683/#leverage-browser-caching-ohne-wordpress-plugin")
        print("###############################")                       

 if (element['localizedRuleName'] == "Prioritize visible content"):
        print("- " + element['localizedRuleName'] + " (" + str((element['ruleImpact']/sum_of_impact)*100) + "%)")
        print("=> Installation des Plugins: wordpress.org/plugins/autoptimize/.")
        print("###############################")                       

 if (element['localizedRuleName'] == "Reduce server response time"):
        print("- " + element['localizedRuleName'] + " (" + str((element['ruleImpact']/sum_of_impact)*100) + "%)")
        print("=> Installation des Plugins: wordpress.org/plugins/p3-profiler/.")
        print("=> Plugins deinstallieren, die nicht wirklich gebraucht werden.")
        print("###############################") 

 if (element['localizedRuleName'] == "Eliminate render-blocking JavaScript and CSS in above-the-fold content"):
        print("- " + element['localizedRuleName'] + " (" + str((element['ruleImpact']/sum_of_impact)*100) + "%)")
        print("=> Installation des Plugins: wordpress.org/plugins/autoptimize/.")
        print("=> Installation des Plugins: wordpress.org/plugins/w3-total-cache/.")
        print("=> Anleitung folgen: http://www.wpbeginner.com/wp-tutorials/how-to-fix-render-blocking-javascript-and-css-in-wordpress/")
        print("###############################") 
