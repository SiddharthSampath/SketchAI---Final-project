from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request,
                  "home/index.html")
def auto(request):
    # context = {}
    # #generator = keras.models.load_model('main/pikay2.h5')
    # if request.method == "POST":
    #
    #     up_image = request.FILES['image']
    #     fs = FileSystemStorage()
    #     name = fs.save(up_image.name,up_image)
    #     # context['url'] = fs.url(name)
    #     # context['url'] = name
    #     context['name'] = name
    #     context['url'] = fs.url(name)
    #     #context['generator'] = generator

    return render(request,"home/auto.html")

def sketch(request):
    context = {}
    #generator = keras.models.load_model('main/pikay2.h5')
    if request.method == "POST":

        up_image = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(up_image.name,up_image)
        # context['url'] = fs.url(name)
        # context['url'] = name
        context['name'] = name
        context['url'] = fs.url(name)
        #context['generator'] = generator

    return render(request,"home/sketch.html",context)

def scenery(request):
    return render(request,
                  "home/scenery.html")
def mountainup(request):
    context = {}
    #generator = keras.models.load_model('main/pikay2.h5')
    if request.method == "POST":

        up_image = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(up_image.name,up_image)
        # context['url'] = fs.url(name)
        # context['url'] = name
        context['name'] = name
        context['url'] = fs.url(name)
        #context['generator'] = generator

    return render(request,"home/mountainup.html",context)

def mountain(request):
    return render(request,
                  "home/mountain.html")


def line(request):
    context = {}
    #generator = keras.models.load_model('main/pikay2.h5')
    if request.method == "POST":

        up_image = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(up_image.name,up_image)
        # context['url'] = fs.url(name)
        # context['url'] = name
        context['name'] = name
        context['url'] = fs.url(name)
        #context['generator'] = generator
    return render(request,
                  "home/line.html",context)

def grayscale(request):
    context = {}
    #generator = keras.models.load_model('main/pikay2.h5')
    if request.method == "POST":

        up_image = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(up_image.name,up_image)
        # context['url'] = fs.url(name)
        # context['url'] = name
        context['name'] = name
        context['url'] = fs.url(name)
        #context['generator'] = generator
    return render(request,
                  "home/grayscale.html",context)
def simplify(request):
    context = {}
    #generator = keras.models.load_model('main/pikay2.h5')
    if request.method == "POST":

        up_image = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(up_image.name,up_image)
        # context['url'] = fs.url(name)
        # context['url'] = name
        context['name'] = name
        context['url'] = fs.url(name)
        #context['generator'] = generator
    return render(request,
                  "home/simplification.html",context)
