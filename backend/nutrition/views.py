from django.shortcuts import render,redirect
from .models import FoodRecord, Food
from django.shortcuts import render
from django.http import HttpResponse

def daily(request):
    all_food = Food.objects.order_by("serving_size")
    return render(request, 'nutrition/daily.html', {"foods": all_food})


def food_record_list(request):
    records = FoodRecord.objects.all()
    date_from = request.GET.get("date_from")
    date_to = request.GET.get("date_to")

    if date_from:
        records = records.filter(created_at__date__gte=date_from)
    if date_to:
        records = records.filter(created_at__date__lte=date_to)

    total_calories = sum(record.calories_consumed for record in records)
    return render(request, "nutrition/food_list.html", {
        "records": records,
        "total_calories": total_calories,
    })


from itertools import combinations

def find_optimal_meal(foods, max_calories):
    foods = sorted(foods, key=lambda x: x.calories, reverse=True)  
    selected = []
    total_calories = 0

    for food in foods:
        if total_calories + food.calories <= max_calories:
            selected.append(food)
            total_calories += food.calories

    return selected

def meal_plan(request):
    max_calories = request.GET.get("calories")
    selected_foods = []

    if max_calories:
        try:
            max_calories = float(max_calories)
            all_foods = Food.objects.all()
            print(all_foods)
            selected_foods = find_optimal_meal(all_foods, max_calories)
        except ValueError:
            pass  

    return render(request, "nutrition/meal-plan.html", {"foods": selected_foods})



def index(request):
    return render(request, 'nutrition/index.html')


def food_delete(request, id):
    record = FoodRecord.objects.get(id=id)
    record.delete()
    return redirect("food_record_list")


def food_record_create(request):
    if request.method == "POST":
        foods = request.POST.getlist("food[]")
        weights = request.POST.getlist("weight[]")
        servings = request.POST.getlist("servings[]")

        for i in range(len(foods)):
            food_id = foods[i]
            weight = weights[i] if weights[i] else None
            servings_count = servings[i] if servings[i] else None

            food = Food.objects.get(id=food_id)
            FoodRecord.objects.create(
                user=request.user,
                food=food,
                weight=weight,
                servings=servings_count
            )

        return redirect("food_record_list") 

    return render(request, "nutrition/food_form.html")


from .forms import FoodForm

def food_create(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("daily")  
    else:
        form = FoodForm()
    
    return render(request, "nutrition/food_create.html", {"form": form})
