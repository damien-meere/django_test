from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_lists.html', context)


def add_item(request):
    if request.method == 'POST':
        # instead of pulling the posted variables outselves, we use the Django form to access them
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
        # name = request.POST.get('item_name')
        # done = 'done' in request.POST
        # Item.objects.create(name=name, done=done)

    form = ItemForm()
    # context contains empty form
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    # get_object_or_404 - used to say we want to get an instance of
    # the item model, with an ID equal to the item ID that was
    # passed into the view via the URL. or it will return 404 error
    item = get_object_or_404(Item, id=item_id)
    # POST handler
    if request.method == 'POST':
        # instead of pulling the posted variables outselves, we use the Django form to access them
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    # create an instance of our item form and return it to the
    # template in the context, pre-populated with the items
    # current details.
    form = ItemForm(instance=item)
    # context contains empty form
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    # just flip the done status
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
