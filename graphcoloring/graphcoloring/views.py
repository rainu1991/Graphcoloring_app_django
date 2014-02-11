from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import json

@csrf_exempt
def graph(request):
    if request.method == 'GET':
        return render_to_response('graph.html')
    elif request.method == 'POST':
        adj = request.POST['adj_data']
        adj_list = json.loads(adj)
        color = {}
        cur_color = 0
        colored_with_cur = {}
        uncolored = sorted(adj_list.items(), key=lambda k: len(k[1]), reverse=True)
        while len(uncolored) > 0:
            first = int(uncolored[0][0])
            del uncolored[0]
            color[first] = cur_color
            colored_with_cur[cur_color] = []
            colored_with_cur[cur_color].append(first)
            for v in uncolored[:]:
                if len(set(v[1]) & set(colored_with_cur[cur_color])) < 1:
                    del uncolored[uncolored.index(v)]
                    cur_vertex = int(v[0])
                    color[cur_vertex] = cur_color
                    colored_with_cur[cur_color].append(cur_vertex)
            cur_color += 1
        return HttpResponse(json.dumps(color))
        

