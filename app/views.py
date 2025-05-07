from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random


def lotto(request):
    numbers=random.sample(range(1,50),6)
    spec_number = random.randint(1,49)
    numbers = sorted(numbers)
    # numbers = " ".join([str(i) for i in numbers])
    numbers = " ".join(map(str, numbers))
    result = {"numbers":numbers, "spec_numbers":spec_number}
    return render(request,"lotto.html", result)
    #return JsonResponse(result)

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello!</h1>")