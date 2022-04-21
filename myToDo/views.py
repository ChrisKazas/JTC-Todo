from django.shortcuts import render
from django.views import View
from .models import ToDoItem, Note, Tags

def handler404(request, exception=None):
    return render(request, '404.html')


def displayTask(self,request):
    self.all_todo_items = ToDoItem.objects.all()

    uncompleted = [task for task in self.all_todo_items if not task.complete]
    completed = [task for task in self.all_todo_items if task.complete]

    return render(
        request=request,
        template_name='list.html',
        context={
            "uncompleted": uncompleted,
            "completed": completed,
            }
    )

# Create your views here.
class Index(View):
    '''Index page'''

    def get(self,request):
        return displayTask(self,request)

    def post(self, request):
        # Adding a Task
        print(request.POST)

        todo_item = request.POST['content']
        tags = {

        }

        if 'urgent' in  request.POST: tags['urgent'] = True
        if 'personal' in  request.POST: tags['personal'] = True
        if 'work' in  request.POST: tags['work'] = True


        new_item = ToDoItem.objects.create(list_item = todo_item)
        for tag in tags.keys():
            if tag == 'urgent': new_item.tags.add(1)
            if tag == 'personal': new_item.tags.add(2)
            if tag == 'work': new_item.tags.add(3)
           
        new_item.save()


        return displayTask(self, request)


class Task(View):
    '''Task page'''

    def get(self,request, id):

        try:
            # Retrieving a Task
            task = ToDoItem.objects.get(id=id)
            notes = ''
            # Get notes for task
            notes = Note.objects.filter(task_id = id)
            # Sort newest to oldest
            notes = sorted(notes,key=lambda note: note.date_created, reverse=True)
        except:
            return render(
            request=request,
            template_name='404.html'
        )


        return render(
            request=request,
            template_name='details.html',
            context={
                "task": task,
                "notes": notes
                }
        )

    def post(self, request, id):

        task = ToDoItem.objects.get(id=id)

        # UPDATE TASK
        if 'update' in request.POST:
            update_item = request.POST['content']
            task = ToDoItem( id = id, list_item = update_item)

        # DELETE TASK
        if 'delete' in request.POST:
            task.delete()
            return displayTask(self,request)

        # MARK TASK AS COMPLETE
        if 'complete' in request.POST:
            task = ToDoItem(id = id , list_item = task.list_item, complete = True)

        # MARK TASK AS COMPLETE
        if 'uncomplete' in request.POST:
            task = ToDoItem(id = id , list_item = task.list_item, complete = False)

        if 'note' in request.POST:
            note_text = request.POST.getlist('note')[0]

            task = ToDoItem.objects.get(id= id)
            note = Note(task = task, note = note_text)
            note.save()

        task.save()

        return displayTask(self,request)








