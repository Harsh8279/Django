from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse("""<h1>Hey I am a Django Server!!</h1>
    #                     <p>Hey This is coming from Django server!!</p>
    #                     <hr>
    #                     <h3>Hope!!</h3>
    #                     """)
    lst_of_names = [
        {
            "name":"Harsh",
            "age":24,
        },
        {
            "name":"Swayam",
            "age":20,
        },
        {
            "name":"Shivaay",
            "age":2,
        },
        {
            "name":"Yash",
            "age":21,
        },
        {
            "name":"Jash",
            "age":21,
        },
        {
            "name":"Vikrant",
            "age":27,
        },
        {
            "name":"Hetarth",
            "age":9,
        },
    ]


    text = """Lorem ipsum, dolor sit amet consectetur adipisicing elit. Laborum asperiores nostrum tempora neque aperiam, sunt excepturi ad itaque dolore quos totam similique reprehenderit rem assumenda. Cumque porro laboriosam sed. Voluptates at hic amet dicta facilis ratione accusamus asperiores quam soluta? Laboriosam minima ex nostrum veritatis quod aliquam exercitationem non! Rerum, alias! Voluptatum sit eveniet impedit, dicta facilis doloribus consequatur vel. Amet pariatur vel labore reiciendis, doloremque obcaecati laudantium fugiat ipsum eveniet officia sunt ducimus nulla recusandae repellendus facere rem sequi enim corporis quia laboriosam eius, alias quam voluptas. Maiores deserunt nobis minima fuga hic fugiat alias tempora quidem qui non."""


    vegies = ["Tomato","potato","kukumber","Onion"]

    return render(request, "home/index.html", context={
        'people':lst_of_names,
        "details":text,
        "vegetables":vegies,
        "page":"Django 2025"
    })

def success_page(request):
    return HttpResponse("<h1>Hey This is the Success Page!!</h1>")


def contact_us(request):
    context = {
        "page":"Contact-Us"
    }
    return render(request,"home/contact.html", context)

def about_us(request):
    context = {
        "page":"About-Us"
    }
    return render(request,"home/about.html", context)