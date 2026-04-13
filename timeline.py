from flask import Flask, render_template_string, jsonify
import json

app = Flask(__name__)

# Load your full timeline JSON data (paste or read from file)
timeline_json = '''{"definition":{"types":[{"id":"defaultNarrative","label":"Narrative Folder","pluralLabel":"Narrative Folders","hasDates":false,"superTypes":[],"properties":["color","image","links","attachments","summary","tags","initials"],"relationshipTypes":["relatesToRef","FLC6vkVrPer8GbthogqJb","ZKrIjbOsiV9pKloryQQIS"],"isLocation":false},{"id":"defaultEvent","label":"Event","pluralLabel":"Events","hasDates":true,"superTypes":["defaultEvent","2h714iHOfUc8ggqONtZdW","LicKTDpWqdMY8IVbmTr3o"],"properties":["color","image","links","attachments","summary","tags","initials"],"relationshipTypes":["relatesToRef","FLC6vkVrPer8GbthogqJb","ZKrIjbOsiV9pKloryQQIS"],"isLocation":false},{"id":"LicKTDpWqdMY8IVbmTr3o","label":"Ère","pluralLabel":"Items","hasDates":true,"superTypes":["LicKTDpWqdMY8IVbmTr3o"],"properties":["color","image","links","attachments","summary","tags","initials"],"relationshipTypes":["relatesToRef","FLC6vkVrPer8GbthogqJb","ZKrIjbOsiV9pKloryQQIS"],"isLocation":false},{"id":"2h714iHOfUc8ggqONtZdW","label":"Période","pluralLabel":"Items","hasDates":true,"superTypes":["2h714iHOfUc8ggqONtZdW","LicKTDpWqdMY8IVbmTr3o"],"properties":["color","image","links","attachments","summary","tags","initials"],"relationshipTypes":["relatesToRef","ZKrIjbOsiV9pKloryQQIS"],"isLocation":false}],"properties":[{"id":"color","label":"Colors","dataFormat":"string","allowedValues":["teal700A","midBlue","grey500","yellow700A","darkPurple","deepOrange500","purple700A","lime500","apple","red700"],"min":null,"max":null,"multiple":false},{"id":"image","label":"Image","dataFormat":"string","allowedValues":null,"min":null,"max":null,"multiple":false},{"id":"links","label":"Links","dataFormat":"string","allowedValues":null,"min":null,"max":null,"multiple":true},{"id":"attachments","label":"Attachments","dataFormat":"string","allowedValues":null,"min":null,"max":null,"multiple":true},{"id":"summary","label":"Summary","dataFormat":"string","allowedValues":null,"min":null,"max":null,"multiple":false},{"id":"tags","label":"Tags","dataFormat":"string","allowedValues":null,"min":null,"max":null,"multiple":true},{"id":"initials","label":"Initials","dataFormat":"string","allowedValues":null,"min":null,"max":null,"multiple":false}],"relationshipTypes":[{"id":"relatesToRef","label":"Relates to","types":["defaultEvent","defaultNarrative","LicKTDpWqdMY8IVbmTr3o","2h714iHOfUc8ggqONtZdW"],"multiple":true},{"id":"FLC6vkVrPer8GbthogqJb","label":"Ère","types":["LicKTDpWqdMY8IVbmTr3o"],"multiple":true},{"id":"ZKrIjbOsiV9pKloryQQIS","label":"Période","types":["2h714iHOfUc8ggqONtZdW"],"multiple":true}],"isRelative":false,"relativeUnits":null,"timescale":"UTC"},"data":{"items":[{"id":"lHxYvfsdzRASISAW74qQq","type":"LicKTDpWqdMY8IVbmTr3o","label":"01 - Pré-Histoire","start":"-1999","latestStart":null,"earliestEnd":null,"end":"0001","ongoing":false,"super":null,"propertyValues":{"color":"red700","links":"","attachments":"","tags":""},"locationUri":null},{"id":"Gix8nPaXgIaULvEwHRw31","type":"LicKTDpWqdMY8IVbmTr3o","label":"02 - Apparition du Cosm","start":"0001","latestStart":null,"earliestEnd":null,"end":"0601","ongoing":false,"super":null,"propertyValues":{"color":"midBlue","links":"","attachments":"","tags":""},"locationUri":null},{"id":"FPGXRYzMHNVJzegw1y5CP","type":"LicKTDpWqdMY8IVbmTr3o","label":"03 - Le monde des gardiens","start":"0601","latestStart":null,"earliestEnd":null,"end":"1601","ongoing":false,"super":null,"propertyValues":{"color":"apple","links":"","attachments":"","tags":""},"locationUri":null},{"id":"Xyg3ARVfUQOAmlYXWbrsZ","type":"LicKTDpWqdMY8IVbmTr3o","label":"04 - Le monde des Cosmers","start":"1601","latestStart":null,"earliestEnd":null,"end":"2201","ongoing":false,"super":null,"propertyValues":{"color":"darkPurple","links":"","attachments":"","tags":""},"locationUri":null},{"id":"OTBEMOcS0bQeui9hiKxY8","type":"2h714iHOfUc8ggqONtZdW","label":"Début de la vie","start":"-1999","latestStart":null,"earliestEnd":null,"end":"-1198","ongoing":false,"super":"lHxYvfsdzRASISAW74qQq","propertyValues":{"color":"deepOrange500","links":"","attachments":"","tags":""},"locationUri":null},{"id":"wYKrQwDdPIuOm9dtn6ysZ","type":"2h714iHOfUc8ggqONtZdW","label":"maturation de la vie","start":"-1198","latestStart":null,"earliestEnd":null,"end":"-0598","ongoing":false,"super":"lHxYvfsdzRASISAW74qQq","propertyValues":{"color":"deepOrange500","links":"","attachments":"","tags":""},"locationUri":null},{"id":"j5rKvI1R1BfMwCvrNvuNK","type":"defaultEvent","label":"Naissance de Astar","start":"0001","latestStart":null,"earliestEnd":null,"end":"0001","ongoing":false,"super":"lHxYvfsdzRASISAW74qQq","propertyValues":{"color":"yellow700A","links":"","attachments":"","tags":""},"locationUri":null},{"id":"BCgjCxRGSBxc5S7nMqgJa","type":"2h714iHOfUc8ggqONtZdW","label":"Test","start":"0101","latestStart":null,"earliestEnd":null,"end":"0132","ongoing":false,"super":"Gix8nPaXgIaULvEwHRw31","propertyValues":{"color":"deepOrange500","links":"","attachments":"","tags":""},"locationUri":null}],"relationships":[{"id":"Y8JemFH4aVoz9LNhY6ZT0","subject":"Gix8nPaXgIaULvEwHRw31","relationshipType":"FLC6vkVrPer8GbthogqJb","target":"lHxYvfsdzRASISAW74qQq"}]},"applicableDate":"2025-11-11","language":null,"@context":null,"appData":{"aeonTimeline":{"openViews":{"byId":{"primaryView":{"viewId":"primaryView","viewType":"TIMELINE_VIEW","timelineOptions":{"unitScale":86104716.69556938,"scrollPosition":{"x":-801,"y":0},"groupIds":[],"collapsedGroups":{}}}},"layout":{"orientation":"ORIENTATION_ROW","viewType":"LAYOUT_VIEW","children":["primaryView"]},"activeView":"primaryView"},"scrollingIsLocked":true,"exposedFilterTypes":["color","type","tags","date"],"filtersById":{"GLOBAL_FILTER_ID":{"filterName":null,"matchCriteria":"filterMatch_ALL","label":{"terms":[],"match":"filterMatch_ANY"},"summary":{"terms":[],"match":"filterMatch_ANY"},"tags":{"terms":[],"match":"filterMatch_ANY"},"type":{"terms":[],"match":"filterMatch_ANY"},"color":{"terms":[],"match":"filterMatch_ANY"},"super":{"terms":[],"match":"filterMatch_ANY"},"date":{"above":null,"below":null,"isAboveIncluded":true,"isBelowIncluded":true},"duration":{"above":null,"below":null,"isAboveIncluded":true,"isBelowIncluded":true},"narrative":{"narrativeStatus":null,"from":null,"to":null},"relationshipsByType":{},"relationshipsByReference":{},"textProperties":{},"numericProperties":{},"boolProperties":{}},"primaryView":{"filterName":null,"matchCriteria":"filterMatch_ALL","label":{"terms":[],"match":"filterMatch_ANY"},"summary":{"terms":[],"match":"filterMatch_ANY"},"tags":{"terms":[],"match":"filterMatch_ANY"},"type":{"terms":[],"match":"filterMatch_ANY"},"color":{"terms":[],"match":"filterMatch_ANY"},"super":{"terms":[],"match":"filterMatch_ANY"},"date":{"above":null,"below":null,"isAboveIncluded":true,"isBelowIncluded":true},"duration":{"above":null,"below":null,"isAboveIncluded":true,"isBelowIncluded":true},"narrative":{"narrativeStatus":null,"from":null,"to":null},"relationshipsByType":{},"relationshipsByReference":{},"textProperties":{},"numericProperties":{},"boolProperties":{}}},"types":{"byId":{"defaultNarrative":{"id":"defaultNarrative","label":"Narrative Folder","pluralLabel":"Narrative Folders","identifierPrefix":"NF","enabled":false,"canDelete":false,"labelDisplayLabel":"Label","startDisplayLabel":"Start","endDisplayLabel":"End","anniversaryDisplayLabel":"Anniversary","extendAnniversaryBeyondEnd":true,"references":{"relatesToRef":true,"FLC6vkVrPer8GbthogqJb":true,"ZKrIjbOsiV9pKloryQQIS":true},"properties":{},"superTypes":{},"canHaveDate":false,"canIncludeInNarrative":true,"showInSequence":false,"showOnSidebar":false,"showAsColumn":false,"columnIsVisible":false,"compactDisplay":"SHORT_LABEL","category":"OTHER","isNarrativeFolder":true,"defaultSequenceType":false,"defaultNarrativeType":false,"canHaveLocationUri":false,"icon":"folder","defaultItemColor":"grey500","quickAccess":"scrollTo"},"defaultEvent":{"id":"defaultEvent","label":"Event","pluralLabel":"Events","identifierPrefix":"EV","enabled":true,"canDelete":true,"labelDisplayLabel":"Label","startDisplayLabel":"Start","endDisplayLabel":"End","anniversaryDisplayLabel":"Anniversary","extendAnniversaryBeyondEnd":true,"references":{"relatesToRef":true,"FLC6vkVrPer8GbthogqJb":true,"ZKrIjbOsiV9pKloryQQIS":true},"properties":{},"superTypes":{"defaultEvent":true,"2h714iHOfUc8ggqONtZdW":true,"LicKTDpWqdMY8IVbmTr3o":true},"canHaveDate":true,"canIncludeInNarrative":true,"showInSequence":true,"showOnSidebar":true,"showAsColumn":false,"columnIsVisible":false,"compactDisplay":"SHORT_LABEL","category":"OTHER","isNarrativeFolder":false,"defaultSequenceType":true,"defaultNarrativeType":false,"canHaveLocationUri":false,"icon":"calendar-star","defaultItemColor":"yellow700A","quickAccess":"scrollTo"},"LicKTDpWqdMY8IVbmTr3o":{"id":"LicKTDpWqdMY8IVbmTr3o","label":"Ère","pluralLabel":"Items","identifierPrefix":"IT","enabled":true,"canDelete":true,"labelDisplayLabel":"label","startDisplayLabel":"date.start","endDisplayLabel":"date.end","anniversaryDisplayLabel":"date.anniversary","extendAnniversaryBeyondEnd":true,"references":{"relatesToRef":true,"FLC6vkVrPer8GbthogqJb":true,"ZKrIjbOsiV9pKloryQQIS":true},"properties":{},"superTypes":{"LicKTDpWqdMY8IVbmTr3o":true},"canHaveDate":true,"canIncludeInNarrative":true,"showInSequence":true,"showOnSidebar":true,"showAsColumn":true,"columnIsVisible":true,"compactDisplay":"SHORT_LABEL","category":"OTHER","isNarrativeFolder":false,"defaultSequenceType":false,"defaultNarrativeType":false,"canHaveLocationUri":false,"icon":"scroll","defaultItemColor":"red700","quickAccess":null},"2h714iHOfUc8ggqONtZdW":{"id":"2h714iHOfUc8ggqONtZdW","label":"Période","pluralLabel":"Items","identifierPrefix":"IT","enabled":true,"canDelete":true,"labelDisplayLabel":"label","startDisplayLabel":"date.start","endDisplayLabel":"date.end","anniversaryDisplayLabel":"date.anniversary","extendAnniversaryBeyondEnd":true,"references":{"relatesToRef":true,"ZKrIjbOsiV9pKloryQQIS":true},"properties":{},"superTypes":{"2h714iHOfUc8ggqONtZdW":true,"LicKTDpWqdMY8IVbmTr3o":true},"canHaveDate":true,"canIncludeInNarrative":true,"showInSequence":true,"showOnSidebar":true,"showAsColumn":true,"columnIsVisible":true,"compactDisplay":"SHORT_LABEL","category":"OTHER","isNarrativeFolder":false,"defaultSequenceType":false,"defaultNarrativeType":false,"canHaveLocationUri":false,"icon":"newspaper","defaultItemColor":"deepOrange500","quickAccess":null}},"sortOrder":{"defaultEvent":2,"defaultNarrative":5,"LicKTDpWqdMY8IVbmTr3o":0,"2h714iHOfUc8ggqONtZdW":1}},"references":{"byId":{"relatesToRef":{"enabled":true,"canDelete":false,"id":"relatesToRef","label":"Relates to","types":{"defaultEvent":true,"defaultNarrative":true,"LicKTDpWqdMY8IVbmTr3o":true,"2h714iHOfUc8ggqONtZdW":true},"icon":"circle filled","color":"mono","lineStyle":"lineStyle_SOLID","bidirectional":true,"inverseLabel":"","showInverse":false,"showInInspector":false},"FLC6vkVrPer8GbthogqJb":{"enabled":true,"canDelete":true,"id":"FLC6vkVrPer8GbthogqJb","label":"Ère","types":{"LicKTDpWqdMY8IVbmTr3o":true},"icon":"circle","color":"mono","lineStyle":"lineStyle_SOLID","bidirectional":false,"inverseLabel":"","showInverse":false,"showInInspector":true},"ZKrIjbOsiV9pKloryQQIS":{"enabled":true,"canDelete":true,"id":"ZKrIjbOsiV9pKloryQQIS","label":"Période","types":{"2h714iHOfUc8ggqONtZdW":true},"icon":"circle","color":"mono","lineStyle":"lineStyle_SOLID","bidirectional":false,"inverseLabel":"","showInverse":false,"showInInspector":true}},"sortOrder":{"relatesToRef":2,"FLC6vkVrPer8GbthogqJb":3,"ZKrIjbOsiV9pKloryQQIS":4}},"disableFiltering":false,"disableFilteringMore":true,"disableSplitView":false,"disableTimelineZoom":false,"skin":"AeonBlue","timelineViewSettings":{"scrollBounds":"infinite","eventLayout":"clearAll","showItemCard":true,"showIdentifier":false,"showDates":true,"showDuration":false,"showNarrative":false,"showRelationshipTypes":["defaultEvent"],"showBlocks":false,"showBlockedBy":false,"showImage":true,"showSummary":true,"showDependencies":true,"showTodayLine":false,"zoomFrom":3,"zoomTo":4,"showTypes":["defaultEvent","LicKTDpWqdMY8IVbmTr3o","2h714iHOfUc8ggqONtZdW"],"showTags":true,"showProperties":[],"showLinks":true,"showRelatedItemTypesOnNewLines":false},"colors":{"byId":{"2AF2A95C-00F9-4A92-BE05-CDD5641D28D5":{"id":"2AF2A95C-00F9-4A92-BE05-CDD5641D28D5","label":"Teal","swatchColor":"teal700A"},"88F01362-D7BA-4AD9-8C93-E0EC45A604B4":{"id":"88F01362-D7BA-4AD9-8C93-E0EC45A604B4","label":"Blue","swatchColor":"midBlue"},"Qrt25SjCVESbmjQdXAEB3":{"id":"Qrt25SjCVESbmjQdXAEB3","label":"Gray","swatchColor":"grey500"},"wuqbqpzSNybZE6OG079do":{"id":"wuqbqpzSNybZE6OG079do","label":"Yellow","swatchColor":"yellow700A"},"FHqCUP6gVd3tqk3hi0b9l":{"id":"FHqCUP6gVd3tqk3hi0b9l","label":"Indigo","swatchColor":"darkPurple"},"D6DB1C49-D913-4D7C-884B-1F7AF1F53187":{"id":"D6DB1C49-D913-4D7C-884B-1F7AF1F53187","label":"Orange","swatchColor":"deepOrange500"},"199ABF77-578A-4EA8-8C2D-8EA080610A78":{"id":"199ABF77-578A-4EA8-8C2D-8EA080610A78","label":"Purple","swatchColor":"purple700A"},"gZkONF7Tn5VMOKWoQ24gk":{"id":"gZkONF7Tn5VMOKWoQ24gk","label":"Lime","swatchColor":"lime500"},"0CAFEDAF-A92E-4012-9E43-438B826F5FC7":{"id":"0CAFEDAF-A92E-4012-9E43-438B826F5FC7","label":"Green","swatchColor":"apple"},"B6D4A6F6-57EA-4E32-8242-5008B57A8AD7":{"id":"B6D4A6F6-57EA-4E32-8242-5008B57A8AD7","label":"Red","swatchColor":"red700"}},"sortOrder":{"0CAFEDAF-A92E-4012-9E43-438B826F5FC7":0,"2AF2A95C-00F9-4A92-BE05-CDD5641D28D5":1,"88F01362-D7BA-4AD9-8C93-E0EC45A604B4":2,"FHqCUP6gVd3tqk3hi0b9l":3,"199ABF77-578A-4EA8-8C2D-8EA080610A78":4,"B6D4A6F6-57EA-4E32-8242-5008B57A8AD7":5,"D6DB1C49-D913-4D7C-884B-1F7AF1F53187":6,"wuqbqpzSNybZE6OG079do":7,"gZkONF7Tn5VMOKWoQ24gk":8,"Qrt25SjCVESbmjQdXAEB3":9}},"tags":{},"properties":{"byId":{},"sortOrder":{}}}}}'''

# Parse JSON string into Python dict
timeline_json = json.loads(timeline_json)
def fix_date(d):
    if not d:
        return None
    if d.startswith('-'):
        # Skip BCE dates for now or adjust properly if needed
        return None
    if d.isdigit():
        return d.zfill(4) + '-01-01'
    return d

def extract_events(data):
    events = []
    if data and 'data' in data and 'items' in data['data']:
        for item in data['data']['items']:
            start = fix_date(item.get('start', None))
            end = fix_date(item.get('end', None))
            if start:
                events.append({
                    'id': item['id'],
                    'content': item.get('label', 'No Label'),
                    'start': start,
                    'end': end,
                    'title': item.get('propertyValues', {}).get('summary', ''),
                    'color': item.get('propertyValues', {}).get('color', '')
                })
    return events

@app.route('/')
def timeline():
    events = extract_events(timeline_json)
    # Template string with embedded JavaScript and vis-timeline from CDN
    html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Python Timeline App</title>
<link href="https://unpkg.com/vis-timeline@7.5.4/styles/vis-timeline-graph2d.min.css" rel="stylesheet" />
<script src="https://unpkg.com/vis-timeline@7.5.4/standalone/umd/vis-timeline-graph2d.min.js"></script>
<style>
#timeline { width: 100%; height: 400px; border: 1px solid lightgray; }
#eventDetails { margin-top: 1rem; font-family: Arial, sans-serif; max-width: 800px; }
</style>
</head>
<body>
<h1>Timeline Visualization</h1>
<div id="timeline"></div>
<div id="eventDetails">Select an event to see details here.</div>
<script>
  const items = new vis.DataSet({{ events | tojson }});
  const options = {stack: true, horizontalScroll: true, zoomKey: 'ctrlKey', tooltip: {followMouse: true}};
  const container = document.getElementById('timeline');
  const timeline = new vis.Timeline(container, items, options);

  const eventDetails = document.getElementById('eventDetails');
  timeline.on('select', function(props) {
    if(props.items.length) {
      let item = items.get(props.items[0]);
      eventDetails.innerHTML = '<h3>' + item.content + '</h3>' +
                               '<p>' + (item.title || '') + '</p>' +
                               '<p><b>Start:</b> ' + item.start + (item.end ? '<br/><b>End:</b> ' + item.end : '') + '</p>';
    } else {
      eventDetails.innerHTML = 'Select an event to see details here.';
    }
  });
</script>
</body>
</html>
'''
    return render_template_string(html_template, events=events)

if __name__ == '__main__':
    app.run(debug=True)
