from django.shortcuts import render, redirect
import random
import markdown2
from . import util
from django.urls import reverse


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    content = util.get_entry(title)

    if not content:
        return render(request,"encyclopedia/error.html", {
            "message": "Solicited page was not found"
        })
    html_content = markdown2.markdown(content)
    if content:
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": html_content
        })

def search(request):
    query = request.GET.get('q')

    content = util.get_entry(query)

    if not content:
        matches = []
        all_entrys = util.list_entries()
        for entry in all_entrys:
            if query.lower() in entry.lower():
                matches.append(entry)
        return render(request, "encyclopedia/matches.html", {
            "matches": matches,
            "query": query
        })

    if content:
        return redirect("wiki", title=query) 

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")

        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html",{
                "message": "This title is already in use"
            })
        util.save_entry(title, desc)
        return redirect("wiki", title=title)
    return render(request, "encyclopedia/create.html")

def randomPage(request):
    all_entries = util.list_entries()

    title = random.choice(all_entries)

    return redirect("wiki", title=title)

def edit(request, title):
    if request.method == "POST":
        content = request.POST.get("edit")

        util.save_entry(title, content)
        return redirect("wiki", title=title)

    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "content": content,
        "title": title
    })

def delete(request):
    if request.method == "POST":
        name = request.POST.get("title")
        title = f"entries/{name}.md"
        if util.default_storage.exists(title):
            util.default_storage.delete(title)
            return render(request, "encyclopedia/index.html", {
                "delete": f"Entry {name} was deleted",
                "entries": util.list_entries()
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "message": "Solicited page was not found"
            })
    return render(request, "encyclopedia/delete.html")
