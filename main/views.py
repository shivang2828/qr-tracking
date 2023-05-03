from django.shortcuts import render,HttpResponse,redirect

count =0

def home(request):
    global count
    return render(request,"home.html", {
          'count':str(count)
      })


def api(request):
    global count
    count +=1
    return redirect("https://qr-tracking.vercel.app/")
